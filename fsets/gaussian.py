from fsets.fuzzy_set import FuzzySet
from math import exp
from interval import Interval

__author__ = ''

class Gaussian(FuzzySet):
    """
    Fuzzy Set with a gaussian function of membership (Bell-shaped function)
    :width: value of bell's width
    :center: x-value which has the greatest value of membership (center of bell)
    :height: biggest value of membership for function (reached on center of bell)
    """

    __slots__ = ('center', 'height', 'width')

    def __init__(self, center, width, height=1):
        interval = Interval(center-width, center+width)
        super(Gaussian, self).__init__(None, interval)
        self.width = width
        self.center = center
        self.height = height

    def __call__(self, x):
        n = x - self.center
        d = self.width
        return self.height*exp(-(n*n)/(2*d*d))

    membership = __call__

    #region defuzzify

    def COG(self, resolution=None):
        return self.center

    def COA(self, precision=0.0000001):
        return self.center

    def CM(self, resolution=None):
        return self.center

    def MM(self, resolution=None):
        return self.center

    def LM(self, resolution=None):
        return self.center

    def RM(self, resolution=None):
        return self.center

    #endregion

    def __repr__(self):
        return 'Gaussian({0}, {1}, {2})'.format(self.center, self.width, self.interval)

    __str__ = __repr__
