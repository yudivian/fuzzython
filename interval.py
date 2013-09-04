from functools import total_ordering

__author__ = ''

@total_ordering
class Interval:
    """
    Represent a real interval [min, max]
    """

    __slots__ = ('_min', '_max')

    def __init__(self, _min=float('-inf'), _max=float('inf')):
        """
        :param _min: lower bound
        :param _max: upper bound
        """
        self._min = _min
        self._max = _max

    @property
    def left(self):
        """
        Gets a left value (minimum) of interval
        """
        return self._min

    @property
    def right(self):
        """
        Gets a right value (maximum) of interval
        """
        return self._max

    @property
    def size(self):
        """
        Gets the length of interval
        """
        return self._max - self._min

    @property
    def middle(self):
        """
        Gets a middle value of interval
        """
        return (self._max - self._min) / 2

    def empty_or_singleton(self):
        """
        Returns true if interval has at most only one number
        """
        return self._min >= self._max

    def singleton(self):
        """
        Returns true if interval has exactly one number
        """
        return self._min == self._max

    def empty(self):
        """
        Returns true if interval is empty
        """
        return self._min > self._max

    def sampling(self, step):
        """
        Gets an enumerable of numbers in interval
        :param step: separation between each number
        """
        if self._min == float('-inf') or self._max == float('inf'):
            yield from (self._min, self._max)
        else:
            current = self._min - step
            _max = self._max
            while current < _max:
                current += step
                yield current

    def __bool__(self):
        return self._min < self._max

    #region Interval operations

    def __contains__(self, item):
        if isinstance(item, Interval):
            return self._min <= item._min and item._max <= self._max
        if isinstance(item, tuple) and len(item)==2:
            return self._min <= item[0] and item[1] <= self._max
            #return self & item == item
        return self._min <= item <= self._max

    def intersect(self, other):
        """
        Gets an intersection of self and other intervals
        :param other: interval or 2-tuple
        """
        #assert isinstance(other, Interval), 'intersect operation is defined only between Intervals'
        if isinstance(other, Interval):
            _min = max(self._min, other._min)
            _max = min(self._max, other._max)
        elif isinstance(other, tuple) and len(other)==2:
            _min = max(self._min, other[0])
            _max = min(self._max, other[1])
        else:
            raise Exception('intersect operation not defined with {0}'.format(type(other)))
        return Interval(_min, _max)

    def union(self, other):
        """
        Gets an union of self and other intervals
        :param other: interval or 2-tuple
        """
        if isinstance(other, Interval):
            if self._min > other._max:
                return Compound(other, self)
            if other._min > self._max:
                return Compound(self, other)
            _min = min(self._min, other._min)
            _max = max(self._max, other._max)
        elif isinstance(other, tuple) and len(other)==2:
            if self._min > other[1]:
                return Compound(Interval(*other), self)
            if other[0] > self._max:
                return Compound(self, Interval(*other))
            _min = min(self._min, other[0])
            _max = max(self._max, other[1])
        else:
            raise Exception('union operation not defined with {0}'.format(type(other)))
        return Interval(_min, _max)

    def __and__(self, other):
        return self.intersect(other)

    def __or__(self, other):
        return self.union(other)

    def __mul__(self, other):
        if isinstance(other, float):
            _min = other*self._min
            _max = other*self._max
            return Interval(_min, _max) if other > 0 else Interval(_max, _min)

    #endregion

    #region Comparisons

    def __lt__(self, other):
        if isinstance(other, Interval):
            if self._min == other._min:
                return self._max < other._max
            return self._min < other._min
        if isinstance(other, tuple) and len(other)==2:
            if self._min == other[0]:
                return self._max < other[1]
            return self._min < other[0]
        return TypeError('Interval unsupported type for comparison')

    def __eq__(self, other):
        if isinstance(other, Interval):
            return self._min == other._min and self._max == other._max
        if isinstance(other, tuple) and len(other)==2:
            return self._min == other[0] and self._min == other[1]
        return False

    #endregion

    def __iter__(self):
        yield from (self._min, self._max)

    def __repr__(self):
        if self.empty(): return 'Empty Interval'
        return 'Interval(%s, %s)' % (self._min, self._max)

    def __str__(self):
        return '({0} .. {1})'.format(self._min, self._max)


class Compound(Interval):
    """
    Represent a Compound Interval which is a list of intervals
    """

    __slots__ = ('_intervals', )

    def __init__(self, *intervals):
        super(Compound, self).__init__()
        self._intervals = []
        self.add_intervals(intervals)

    def add_interval(self, interval):
        if not interval.empty() and interval not in self._intervals:
            self._intervals.append(interval)
            self._intervals.sort()
            self._min = self._intervals[0]._min
            self._max = self._intervals[-1]._max

    def add_intervals(self, intervals):
        for interval in intervals:
            self.add_interval(interval)

    def __contains__(self, item):
        for interval in self._intervals:
            if item in interval:
                return True
        return False

    def empty(self):
        if not self._intervals:
            return True
        for interval in self._intervals:
            if not interval.empty():
                return False
        return True

    def intersect(self, other):
        if isinstance(other, Compound):
            #if self._min > other._max or self._max < other._min:
                #return Interval()
            res = []
            for other_interval in other._intervals:
                for interval in self._intervals:
                    intersection = interval.intersect(other_interval)
                    if not intersection.empty():
                        res.append(intersection)
            return Compound(*res)
        #if isinstance(other, Interval):
        res = []
        for interval in self._intervals:
            intersection = interval.intersect(other)
            if not intersection.empty():
                res.append(intersection)
        return Compound(*res)


    def union(self, other):
        if isinstance(other, Compound):
            res = []
            for other_interval in other._intervals:
                for interval in self._intervals:
                    union = interval.union(other_interval)
                    if union.empty():
                        continue
                    if isinstance(union, Compound):
                        for i in union._intervals:
                            res.append(i)
                    else:
                        res.append(union)
            return Compound(*res)

        res = []
        for interval in self._intervals:
            union = interval.union(other)
            if union.empty():
                continue
            if isinstance(union, Compound):
                for i in union._intervals:
                    res.append(i)
            else:
                res.append(union)
        return Compound(*res)

    def __iter__(self):
        yield from self._intervals

    def __repr__(self):
        if self.empty():
            return 'Empty Compound Interval'
        s = map(repr, self._intervals)
        return 'Compound: ' + ' U '.join(s)

    __str__ = __repr__


