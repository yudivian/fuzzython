from fsets.fuzzy_set import FuzzySet
from interval import Interval
from norms.norms import minimum

__author__ = ''


class Polygon(FuzzySet):
    """
    List of points connected each pair by rect
    """

    __slots__ = ('_points', '_lines')
    X, Y = 0, 1

    def __init__(self, *points):
        super(Polygon, self).__init__(None, None)
        self._points = []
        #self._lines = []
        if points:
            self.add_points(points)

    @staticmethod
    def _quick_build_(points):
        p = Polygon()
        p.interval = Interval(points[0][Polygon.X], points[-1][Polygon.X])
        p._points = points
        return p

    def __call__(self, x):
        """Gets membership for value x"""
        points = self._points
        if not points:
            return 0.0
        if len(points)==1 or x <= points[0][Polygon.X]:
            return points[0][Polygon.Y]
        if x >= points[-1][Polygon.X]:
            return points[-1][Polygon.Y]

        for pos, point in enumerate(points):
            if point[Polygon.X] > x:
                break
        else:
            raise Exception('interval not found')
        start = points[pos-1]

        #return Polygon.Rect.build_from(start, point)(x)
        sx, sy = start
        px, py = point
        m = (py - sy) / (px - sx)
        n = sy - m*sx
        return m*x + n

    membership = __call__

    #region Set operations: union, intersection, complement

    def complement(self, cnorm=None):
        cnorm = self.cnorm or FuzzySet._CNORM_
        points = [(x, cnorm(y)) for x,y in self._points]
        return Polygon._quick_build_(points)

    #endregion

    #region fuzzify

    def fuzzify_with(self, other):
        if not isinstance(other, Polygon):
            return super(Polygon, self).fuzzify_with(other)
        interval = self.interval.intersect(other.interval)
        if interval.empty():
            return 0.0
        xs = self.merge_points(other)
        membership = self.membership
        tnorm = self.tnorm
        max_ = 0
        for x in xs:
            max_ = max(max_, tnorm(membership(x), other(x)))
        return max_

    #endregion

    #region defuzzifying methods

    def COG(self, resolution=None):
        # --- Computes I x*P(x) ---
        (px, py), *points = self._points
        IxPx = 0.0
        for x, y in points:
            # rect between (px,py), (x,y)
            m = (y - py)/ (x - px)
            n = py - m*px
            #f(x) = m*x*x*x/3 + n*x*x/2
            I = lambda x: x*x*(m*x/3 + n/2)
            IxPx += I(x) - I(px)
            px, py = x, y

        IPx = self.area(resolution)
        return IxPx / IPx


    def MM(self, resolution=None):
        points = self._points
        xmax, ymax = [], float('-inf')
        for x,y in points:
            if y > ymax:
                ymax = y
                xmax = [x]
            elif y== ymax:
                xmax.append(x)
        return sum(xmax) / len(xmax)

    def LM(self, resolution=None):
        points = self._points
        xmax, ymax = None, float('-inf')
        for x,y in points:
            if y > ymax:
                ymax = y
                xmax = x
        return xmax

    def RM(self, resolution=None):
        points = self._points
        xmax, ymax = None, float('-inf')
        for x,y in points:
            if y >= ymax:
                ymax = y
                xmax = x
        return xmax

    #endregion

    #region Function operations

    def minimize(self, other):
        if not callable(other):
            points = self._points
            px, py = points[0]
            points_ = [(px, min(py, other))]
            for x, y in points[1:]:
                if py < other or y < other:
                    rect = Polygon.Rect.build_from((px, py), (x,y))
                    rx = rect.get_x(other)
                    if rx is not None and px < rx < x:
                        points_.append((rx, other))

                points_.append((x, min(y, other)))
                px, py = x, y

            return Polygon._quick_build_(points_)

        return self._operation(minimum, other)


    def _operation(self, op, other):
        if isinstance(other, Polygon):
            # xs = sorted({x for x,_ in self._points + other._points})
            xs = self.merge_points(other)
            points = [(x, op(self(x),other(x))) for x in xs]
            return Polygon._quick_build_(points)
        if not callable(other):
            points = [(x,op(y,other)) for x,y in self._points]
            return Polygon._quick_build_(points)
        return super(Polygon,self)._operation(op, other)

    def _operation_(self, other, op):
        if not callable(other):
            points = [(x,op(other,y)) for x,y in self._points]
            return Polygon._quick_build_(points)
        return super(Polygon,self)._operation_(other, op)

    #endregion

    #region Function stuff

    def merge_points(self, other):
        """
        Merge points from two Polygons including intersection points from lines
        :param other: Polygon
        """
        if self._points and other._points:
            xs = sorted({x for x,_ in self._points + other._points})
            xs_ = []
            prev = xs[0]
            for x in xs[1:]:
                rect1 = Polygon.Rect.build_from((prev, self(prev)), (x, self(x)))
                rect2 = Polygon.Rect.build_from((prev, other(prev)), (x, other(x)))
                xi = rect1.intersect(rect2)

                if xi is not None:
                    if prev < xi < x:
                        xs_.append(xi)
                prev = x

            for x_ in xs_:
                for index, x in enumerate(xs):
                    if x_ < x:
                        xs.insert(index, x_)
                        break
            return xs
        else:
            return self._points or other._points

    def area(self, resolution=None):
        points = self._points
        px, py = points[0]
        area = 0.0
        for x, y in points[1:]:
            # rect from (px,py), (x,y)
            m = (y - py) / (x - px)
            n = py - m*px
            # f(x) = m*x*x/2 + n*x
            I = lambda x: x*(m*x*0.5 + n)
            area += I(x) - I(px)
            px, py = x, y
        return area

    def area_(self, a, b):
        points = self._points
        if not points:
            return 0.0
        if len(points) == 1:
            return points[0][Polygon.Y]*(b - a)

        area = 0.0
        px, py = points[0]
        if a < px:
            area = py*(px - a)
            a = px

        for x, y in points[1:]:
            if a < x:
                #rect from (px,py), (x,y)
                m = (y - py)/ (x - px)
                n = py - m*px
                I = lambda x: (m*x*0.5 + n)*x
                if b <= x:
                    return area + (I(b) - I(a)) #area(a, b)
                area += I(x) - I(a) #area(a, x)
                a = x
            px, py = x, y

        return area

    def add_points(self, points):
        for p in points:
            self.add_point(p)

    def add_point(self, point):
        """
        Adds a point to polygon list of points in correct position
        :param point: new point to addition
        """
        X, Y = Polygon.X, Polygon.Y
        points = self._points

        for index, p in enumerate(self._points):
            if point[X] == p[X]:
                point = (point[X], max(point[Y], p[Y]))
                points[index] = point
                break
            if point[X] < p[X]:
                points.insert(index, point)
                break
        else:
            points.append(point)
            # self._lines = []

        self.interval = Interval(points[0][Polygon.X], points[-1][Polygon.X])

    def clear(self):
        """
        Clears the polygon list of points
        """
        self._points.clear()
        self.interval = None

    def get_polygon(self):
        """
        Returns a Polygon represent current instance
        """
        return self

    @staticmethod
    def create_from(function, a, b, sampling):
        """
        Creates a Polygon from a function in the interval (a, b)
        with a given sampling of points
        :param function: any function (callable)
        :param a: start of interval
        :param b: end of interval
        :param sampling: number of points from interval (a,b)
        """
        if isinstance(function, Polygon):
            return function.get_polygon()
        step = (b-a)/sampling
        points = []
        x = a
        while x <= b:
            y = function(x)
            points.append((x,y))
            x += step
        return Polygon(*points)

    def __bool__(self):
        return len(self._points) > 0

    def __getitem__(self, item):
        return self._points[item]

    def __setitem__(self, key, value):
        if isinstance(key, float) or key >= len(self._points):
            if isinstance(value, tuple):
                raise ValueError('')
            for index, (x, _) in enumerate(self._points):
                if x == key:
                    self._points[index] = (x, value)
                    break
            else:
                self._points.append((key, value))
                self._points.sort()
        else:
            self._points[key] = value
            self._points.sort()

    def __delitem__(self, key):
        del self._points[key]

    def __iter__(self):
        yield from self._points

    #endregion

    #region Rect

    class Rect(object):
        """ y = m*x + n """

        __slots__ = ('m', 'n')

        def __init__(self, m=1, n=0):
            self.m = m
            self.n = n

        def __call__(self, x):
            return self.m*x + self.n

        def area(self, a, b):
            m, n = self.m, self.n
            I = lambda x: m*x*x/2 + n*x
            return I(b) - I(a)

        @staticmethod
        def build_from(point1, point2):
            x1, y1 = point1
            x2, y2 = point2
            m = (y2 - y1)/ (x2 - x1)
            n = y1 - m*x1
            return Polygon.Rect(m, n)

        def intersect(self, other):
            if self.m == other.m:
                #return self if  self.n == other.n else None
                return None
            x = (other.n - self.n) / (self.m - other.m)
            return x

        def get_x(self, y):
            return (y - self.n) / self.m if self.m else None

        def __repr__(self):
            return 'Rect y = {0}*x + {1}'.format(self.m, self.n)

    #endregion

    def __repr__(self):
        s = map(repr, self._points)
        return 'Polygon(' + ', '.join(s) + ')'

    def __str__(self):
        s = map(str, self._points)
        return ' '.join(s)

