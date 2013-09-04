from fsets.fuzzy_set import FuzzySet
from interval import Interval

__author__ = ''

class Singleton(FuzzySet):
    """
    Fuzzy Set with an only element of universe with membership above zero
    """

    __slots__ = ('x', 'y')

    def __init__(self, x=0.0, y=1.0):
        """
        Initialize a singleton
        :param x: element with membership different of zero
        :param y: degree of membership for the x-element
        """
        super(Singleton, self).__init__(None, None)
        self.interval = Interval(x,x)
        self.x = x
        self.y = y

    def __call__(self, x):
        return self.y if x==self.x else 0.0

    #region fuzzify

    def fuzzify_with(self, other):
        return self.tnorm(self.y, other(self.x))

    #endregion

    #region defuzzifying methods

    def COG(self, resolution=100):
        return self.x

    def COA(self, precision=0.0000001):
        return self.x

    def MM(self, resolution=None):
        return self.x

    def CM(self, resolution=None):
        return self.x

    def LM(self, resolution=100):
        return self.x

    def RM(self, resolution=100):
        return self.x

    #endregion

    #region Function operations
    # use the Fuzzy Set class implementation
    #endregion

    #region Function stuff

    def area(self, resolution=None):
        return 0.0

    def area_(self, a, b):
        return 0.0

    #endregion

    def __repr__(self):
        return 'Singleton({0},{1})'.format(self.x, self.y)

    def __str__(self):
        return str(self.x)
