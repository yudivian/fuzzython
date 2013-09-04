from fsets.polygon import Polygon
from interval import Interval

__author__ = ''

class Triangular(Polygon):
    """
    Fuzzy Set with Triangular-shape function defined with a, b, and c points
              .
             /|\
            / | \
           /  |  \
         _/   |   \_
          |   b   |
          a       c
    """

    __slots__ = ('_rect_ab', '_rect_bc')

    def __init__(self, a, b, c=None):
        super(Triangular, self).__init__()
        if c is None:
            c = (b[0]+(b[0]-a[0]), a[1])
        self._rect_ab = Polygon.Rect.build_from(a, b)
        self._rect_bc = Polygon.Rect.build_from(b, c)
        self._points = [a, b, c]
        self.interval = Interval(a[0], c[0])

    def __call__(self, x):
        p1, p2, p3 = self._points
        x1, y1 = p1
        if x <= x1:
            return y1
        x2 = p2[Polygon.X]
        if x < x2:
            return self._rect_ab(x)
        x3, y3 = p3
        if x < x3:
            return self._rect_bc(x)
        return y3

    membership = __call__

    #region Function stuff

    def add_point(self, point):
        p1, p2, p3 = self._points
        polygon = Polygon(p1, p2, p3, point)
        return polygon

    def add_points(self, points):
        p1, p2, p3 = self._points
        polygon = Polygon(p1, p2, p3, *points)
        return polygon

    def clear(self):
        return Polygon()

    def get_polygon(self):
        return Polygon(*self._points)

    @staticmethod
    def built_from(x_min, x_mid, x_max, y_min=0, y_max=1):
        """
        Gets a triangular function
              .------ y_max=1
             /|\
            / | \
           /  |  \
         _/   |   \_  y_min=0
          | x_mid |
          |   |   |
        x_min | x_max
        """
        a = (x_min, y_min)
        b = (x_mid, y_max)
        c = (x_max, y_min)
        return Triangular(a, b, c)

    #endregion

    #region Function operations

    def _operation(self, op, other):
        if isinstance(other, Polygon):
            xs = self.merge_points(other)
            points = [(x, op(self(x),other(x))) for x in xs]
            return Polygon(*points)
        if not callable(other):
            points = [(x, op(y,other)) for x,y in self._points]
            return Triangular(*points)
        return super(Triangular,self)._operation(op, other)

    def _operation_(self, other, op):
        if not callable(other):
            points = [(x, op(other,y)) for x,y in self._points]
            return Triangular(*points)
        return super(Triangular,self)._operation_(other, op)

    #endregion

    def __repr__(self):
        return 'Triangular({0}, {1}, {2})'.format(*self._points)

    #__str__ = __repr__

