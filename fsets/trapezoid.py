from fsets.polygon import Polygon
from interval import Interval

__author__ = ''

class Trapezoid(Polygon):
    """
    Trapezoid-shape function defined with points a, b, c and d
               _____
              /     \
             /|     |\
            / |     | \
           /  |     |  \
         _/   |     |   \_
          |   b     c   |
          a             d
    """

    __slots__ = ('_rect_ab', '_rect_bc', '_rect_cd')

    def __init__(self, a, b, c, d):
        super(Trapezoid, self).__init__()
        self._rect_ab = Polygon.Rect.build_from(a, b)
        self._rect_bc = Polygon.Rect.build_from(b, c)
        self._rect_cd = Polygon.Rect.build_from(c, d)
        self._points = [a, b, c, d]
        self.interval = Interval(a[0], d[0])

    def __call__(self, x):
        (x1, y1), p2, p3, (x4, y4) = self._points
        if x <= x1:
            return y1
        x2 = p2[Polygon.X]
        if x <= x2:
            return self._rect_ab(x)
        x3 = p3[Polygon.X]
        if x <= x3:
            return self._rect_bc(x)
        if x < x4:
            return self._rect_cd(x)
        return y4

    membership = __call__

    #region defuzzify

    def COG(self, resolution=None):
        a, b, c, d = self._points
        if b[1] == c[1]:
            return sum(b[0]+c[0])/2
        return super().COG(resolution)

    def COA(self, precision=0.0000001):
        a, b, c, d = self._points
        if b[1] == c[1]:
            return sum(b[0]+c[0])/2
        return super().COA(precision)

    def CM(self, resolution=None):
        a, b, c, d = self._points
        if b[1] == c[1]:
            return sum(b[0]+c[0])/2
        return super().CM(resolution)

    def MM(self, resolution=None):
        a, b, c, d = self._points
        if b[1] == c[1]:
            return sum(b[0]+c[0])/2
        return super().MM(resolution)

    #endregion

    #region Function stuff

    def add_point(self, point):
        p1, p2, p3, p4 = self._points
        polygon = Polygon(p1, p2, p3, p4, point)
        return polygon

    def add_points(self, points):
        p1, p2, p3, p4 = self._points
        polygon = Polygon(p1, p2, p3, p4, *points)
        return polygon

    def clear(self):
        return Polygon()

    def get_polygon(self):
        return Polygon(*self._points)

    #endregion

    #region Function operations

    def _operation(self, op, other):
        if isinstance(other, Polygon):
            xs = self.merge_points(other)
            points = [(x, op(self(x),other(x))) for x in xs]
            return Polygon(*points)
        if not callable(other):
            points = [(x, op(y,other)) for x,y in self._points]
            return Trapezoid(*points)
        return super(Trapezoid,self)._operation(op, other)

    def _operation_(self, other, op):
        if not callable(other):
            points = [(x, op(other,y)) for x,y in self._points]
            return Trapezoid(*points)
        return super(Trapezoid,self)._operation_(other, op)

    #endregion

    def __repr__(self):
        return 'Trapezoid({0[0]}, {0[1]}, {0[2]}, {0[3]})'.format(self._points)

    #__str__ = __repr__

