from fsets.fuzzy_set import FuzzySet
from interval import Interval

__author__ = ''

class SFunction(FuzzySet):
    """
    Fuzzy Set with a S-shaped function
             __
            /|
           / |
          /| |
       __/ | |
         | b |
         a   c

    a: point for minimum function evaluation
    b: x-value for middle function evaluation
    c: point for maximum function evaluation
    """

    __slots__ = ('a', 'b', 'c')

    def __init__(self, a, b, c):
        super(SFunction, self).__init__(None, None)
        self.interval = Interval(a[0], c[0])
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x):
        (ax, ay), b, (cx, cy) = self.a, self.b, self.c
        if x <= ax:
            return ay
        elif x <= b:
            num = (x-ax)/(cx-ax)
            return 2*num*num
        elif x < cx:
            num = (x-cx)/(cx-ax)
            return 1-2*num*num
        else:
            return cy

    membership = __call__

    #region Set operations: union, intersection, complement
    # use the Fuzzy Set class implementation
    #endregion

    #region defuzzifying methods

    def CM(self, resolution=None):
        return self.c[0]

    def MM(self, resolution=None):
        return self.c[0]

    def LM(self, resolution=None):
        return self.c[0]

    def RM(self, resolution=None):
        return self.c[0]

    #endregion

    #region Function operations

    def _operation(self, op, other):
        if not callable(other):
            (ax, ay), b, (cx, cy) = self.a, self.b, self.c
            a = ax, op(ay, other)
            c = cx, op(cy, other)
            return SFunction(a, b, c)
        return super(SFunction,self)._operation(op, other)

    def _operation_(self, other, op):
        if not callable(other):
            (ax, ay), b, (cx, cy) = self.a, self.b, self.c
            a = ax, op(other, ay)
            c = cx, op(other, cy)
            return SFunction(a, b, c)
        return super(SFunction,self)._operation_(other, op)

    #endregion

    #region Function stuff
    # use the Fuzzy Set class implementation
    #endregion

    def __repr__(self):
        return 'SFunction({0},{1},{2})'.format(self.a, self.b, self.c)

    __str__ = __repr__

