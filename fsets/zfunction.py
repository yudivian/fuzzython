from fsets.sfunction import SFunction

__author__ = ''

class ZFunction(SFunction):
    """
    Fuzzy Set with a Z-shaped function
       __
        |\
        | \
        | |\
        | | \__
        | b |
        a   c

    a: point for maximum function evaluation
    b: x-value for middle function evaluation
    c: point for minimum function evaluation
    """

    __slots__ = ()

    def __init__(self, a, b, c):
        super(ZFunction, self).__init__(a,b,c)

    def __call__(self, x):
        return 1 - SFunction.__call__(self, x)

    # def area(self, a, b, resolution=None):
    #     return (b - a) - super().area(a, b, resolution)

    def __repr__(self):
        return 'ZFunction({0},{1},{2})'.format(self.a, self.b, self.c)

    __str__ = __repr__
