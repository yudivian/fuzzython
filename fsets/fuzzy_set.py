"""
Module FuzzySet...
"""
from functools import reduce
from norms.norms import minimum, maximum, zadeh_complement
from operator import add, mul, sub, truediv, pow

__author__ = ''


class FuzzySet(object):
    """
    Represent a Fuzzy Set with a any membership function
    :function: lambda expression
    :interval: interval for defuzzification method and area calculation
    :tnorm: t-norm used for conjunction operations
    :snorm: s-norm used for disjunction operations
    :cnorm: t-norm used for complement operations
    :_RESOLUTION_: resolution is the number of intervals for function area calculation
    :_TNORM_: default t-norm
    :_SNORM_: default s-norm
    :_CNORM_: default c-norm
    """
    __slots__ = ('function', 'interval', 'tnorm', 'snorm', 'cnorm')

    _RESOLUTION_ = 100
    _CNORM_ = zadeh_complement
    _TNORM_ = minimum
    _SNORM_ = maximum

    def __init__(self, function, interval, tnorm=None, snorm=None, cnorm=None):
        """
        Initialize a fuzzy set
        :param function: lambda expression
        :param interval: support interval used for defuzzification method
        :param cnorm: norm used for complement
        :param tnorm: norm used for intersection
        :param snorm: norm used for union
        """
        self.tnorm = tnorm or FuzzySet._TNORM_
        self.snorm = snorm or FuzzySet._SNORM_
        self.cnorm = cnorm or FuzzySet._CNORM_
        self.function = function
        self.interval = interval

    def __call__(self, x:float) -> float:
        """
        Gets the membership value for an element in the set
        :param x: element of universe
        :return: float value between 0 and 1
        """
        if self.function:
            return self.function(x)
        return 0.0

    membership = __call__

    # region Set operations: union, intersection, negation

    @staticmethod
    def conjunction(*fuzzy_sets, tnorm=None):
        """
        Compute the conjunction of several fuzzy set with a custom tnorm
        :param fuzzy_sets: more than one fuzzy set is required
        :param tnorm: norm used for conjunction
        """
        return reduce(lambda s1,s2: s1.intersect(s2, tnorm), fuzzy_sets)

    @staticmethod
    def disjunction(*fuzzy_sets, snorm=None):
        """
        Compute the disjunction of several fuzzy set with a custom tnorm
        :param fuzzy_sets: more than one fuzzy set is required
        :param snorm: norm used for disjunction
        """
        return reduce(lambda s1,s2: s1.union(s2, snorm), fuzzy_sets)

    def intersect(self, other, tnorm=None):
        """
        Compute the intersection between current fuzzy set and other fuzzy set
        :param other: second fuzzy set
        :param tnorm: norm used for intersection
        """
        # assert isinstance(other, FuzzySet), 'intersect operation is defined only between fuzzy sets'
        tnorm = tnorm or self.tnorm
        fset = self._operation(tnorm, other)
        fset.interval = self.interval.intersect(other.interval)
        return fset

    def union(self, other, snorm=None):
        """
        Compute the union between current fuzzy set and other fuzzy set
        :param other: second fuzzy set
        :param snorm: norm used for union
        """
        # assert isinstance(other, FuzzySet), 'union operation is defined only between fuzzy sets'
        snorm = snorm or self.snorm
        fset = self._operation(snorm, other)
        fset.interval = self.interval.union(other.interval)
        return fset

    def complement(self, cnorm=None):
        """
        Compute the complement of current fuzzy set
        :param cnorm: norm used for complement
        """
        cnorm = cnorm or self.cnorm
        function = lambda x: cnorm(self.function(x))
        norms = self.norms()
        return FuzzySet(function, self.interval, *norms)

    def __and__(self, other):
        return self.intersect(other)

    def __or__(self, other):
        return self.union(other)

    def __invert__(self):
        return self.complement()

    # endregion

    #region fuzzify

    def fuzzify_with(self, other):
        """
        Get the fuzzifycation value for other fuzzy set on this one
        :param other: fuzzy set
        """
        from fsets.singleton import Singleton
        if isinstance(other, Singleton):
            return self.tnorm(self.membership(other.x), other.y)

        interval = self.interval.intersect(other.interval)
        if interval.empty():
            return 0.0
        a, b = interval
        step = (b-a)/FuzzySet._RESOLUTION_
        membership = self.membership
        tnorm = self.tnorm
        max_ = 0
        while a <= b:
            max_ = max(max_, tnorm(membership(a), other(a)))
            a += step
        return max_

    #endregion

    # region defuzzifying methods

    def COG(self, resolution=None):
        """
        Returns center of gravity (C.O.G)

        :param resolution: number of intervals to calculate integrals
        :return: x-value of C.O.G
        """
        f = self.function or self.__call__
        xf = FuzzySet(lambda x: x* f(x), self.interval, *self.norms())
        IxFx = xf.area(resolution)
        IFx = self.area(resolution)
        return IxFx / IFx

    def COA(self, precision=0.0000001):
        """
        Returns center (bisector) of area (C.O.A), the x-point in which
        the area at both sides is equal

        :param precision: maximum tolerance for compare areas
        :return: x-value of C.O.A
        """
        start, end = self.interval
        center = (start + end) / 2
        left, right = 0, 0
        left_ = left + self.area_(start, center)
        right_ = right + self.area_(center, end)
        while abs(right_ - left_) >= precision:
            if left_ > right_:
                right = right_
                end = center
            elif right_ > left_:
                start = center
                left = left_
            else:
                return center
            center = (start + end) / 2
            left_ = left + self.area_(start, center)
            right_ = right + self.area_(center, end)
        # return self._COA(start, end)
        return center

    def _COA(self, start, end, left=0, right=0):
        center = (start + end) / 2
        left_ = left + self.area_(start, center)
        right_ = right + self.area_(center, end)

        if abs(right_ - left_) < 0.0000001:
            return center

        if left_ > right_:
            return self._COA(start, center, left, right_)

        if right_ > left_:
            return self._COA(center, end, left_, right)

    def CM(self, resolution=None):
        """
        Returns center of maximum (C.M)
        :return: x-value of C.M
        """
        left = self.LM(resolution)
        right = self.RM(resolution)
        return (left+right) / 2

    def MM(self, resolution=None):
        """
        Returns mean of maximum (M.M)
        :return: x-value of M.O.M
        """
        resolution = resolution or FuzzySet._RESOLUTION_
        f = self.function or self.__call__
        a, b = self.interval
        step = (b - a) / resolution

        xs, y = [a], 0
        while a < b:
            y_a = f(a)
            if y_a > y:
                xs, y = [a], y_a
            elif y_a == y:
                xs.append(a)
            a += step
        return sum(xs)/len(xs)

    def LM(self, resolution=None):
        """
        Returns the left of maximum (L.M)
        :param resolution:
        """
        resolution = resolution or FuzzySet._RESOLUTION_
        f = self.function or self.__call__
        a, b = self.interval
        step = (b - a) / resolution

        x, y = a, 0
        while a < b:
            y_a = f(a)
            if y_a > y:
                x, y = a, y_a
            a += step
        return x

    def RM(self, resolution=None):
        """
        Returns the right of maximum (R.M)
        :param resolution:
        """
        resolution = resolution or FuzzySet._RESOLUTION_
        f = self.function or self.__call__
        a, b = self.interval
        step = (b - a) / resolution

        x, y = a, 0
        while a < b:
            y_a = f(a)
            if y_a >= y:
                x, y = a, y_a
            a += step
        return x

    # endregion

    #region Function operations: add, mul, sub, div, pow

    def activate(self, norm, other):
        """
        Gets the activation fuzzy set for given norm and other value
        """
        if norm == minimum:
            return self.minimize(other)
        return self._operation(norm, other)

    def minimize(self, other):
        """
        Gets a fuzzy set resulting of minimize with other value or fuzzy set
        """
        return self._operation(minimum, other)

    def maximize(self, other):
        """
        Gets a fuzzy set resulting of maximize with other value or fuzzy set
        """
        return self._operation(maximum, other)

    def _operation(self, op, other):
        """
        Gets a fuzzy set resulting of apply the operator op between
        current fuzzy set and the other instance
        """
        f = self.function or self.__call__
        f_ = (lambda x: op(f(x), other(x))) if callable(other) else (lambda x: op(f(x), other))
        return FuzzySet(f_, self.interval, *self.norms())

    def _operation_(self, other, op):
        """
        Gets a fuzzy set resulting of apply the operator op between
        the other instance and current fuzzy set
        """
        f = self.function or self.__call__
        f_ = (lambda x: op(other(x), f(x))) if callable(other) else (lambda x: op(other, f(x)))
        return FuzzySet(f_, self.interval, *self.norms())

    def __add__(self, other):
        return self._operation(add, other)

    __radd__ = __add__

    def __sub__(self, other):
        return self._operation(sub, other)

    def __rsub__(self, other):
        return self._operation_(other, sub)

    def __mul__(self, other):
        return self._operation(mul, other)

    __rmul__ = __mul__

    def __truediv__(self, other):
        return self._operation(truediv, other)

    def __rtruediv__(self, other):
        return self._operation_(other, truediv)

    def __pow__(self, power, modulo=None):
        if modulo is not None:
            pass
        return self._operation(pow, power)

    def __rpow__(self, power, modulo=None):
        if modulo is not None:
            pass
        return self._operation_(power, pow)

    #endregion

    #region Function stuff

    def area(self, resolution=None) -> float:
        """
        Calculates the area beneath curve in interval (a,b)
        defined integral of current function
        """
        resolution = resolution or FuzzySet._RESOLUTION_
        a, b = self.interval
        step = (b-a)/resolution
        f = self.function or self.__call__
        area = 0
        y1 = f(a)
        while a < b:
            a += step
            y2 = f(a)
            #area += min(y1, y2)*step + step*abs(y2-y1)/2
            area += (y1+y2)*step/2
            y1 = y2
        return area

    def area_(self, a, b):
        """
        Calculates the area beneath curve in interval given by (a,b)
        defined integral of current function
        :param a: left x
        :param b: right x
        """
        step = (b-a)/FuzzySet._RESOLUTION_
        f = self.function or self.__call__
        area = 0
        y1 = f(a)
        while a < b:
            a += step
            y2 = f(a)
            area += (y1+y2)*step/2
            y1 = y2
        return area

    def coordinates(self, resolution=None):
        """
        Gets an enumerable of function pairs (x, y) in the interval
        of function
        :param resolution: number of pairs in function interval
        """
        resolution = resolution or FuzzySet._RESOLUTION_
        a, b = self.interval
        step = (b-a)/resolution
        function = self.function
        while a < b:
            yield a, function(a)
            a += step

    #endregion

    def norms(self):
        """
        Gets three norms used for operations between fuzzy sets for current
        instance... intersection, union and complement
        """
        return self.tnorm, self.snorm, self.cnorm

    def __iter__(self):
        yield from (self.tnorm, self.snorm, self.cnorm)

    def __repr__(self):
        return 'Fuzzy Set'

    __str__ = __repr__

