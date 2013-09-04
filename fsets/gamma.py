from math import exp
from fsets.fuzzy_set import FuzzySet

__author__ = ''

class Gamma(FuzzySet):
    """
    Fuzzy Set with gamma membership function (V-shaped function)
      __     __
        \   /
         \ /
          |
        value
    :value: x-value where function reach it's minimum value: 0
    :k: indicates the opening of V-shape.
        Bigger values of k make V-shape close to I-shape
        k-value must be positive
    """

    __slots__ = ('value', 'k')

    def __init__(self, value, k, interval):
        super(Gamma, self).__init__(None, interval)
        self.value = value
        self.k = k

    def __call__(self, x):
        if x <= self.value: return 0.0
        v = x-self.value
        return 1 - exp(-self.k*v*v)

    membership = __call__

    #region defuzzify

    def MM(self, resolution=None):
        left, right = self.interval
        yleft = self.__call__(left)
        yright = self.__call__(right)
        if yleft == yright:
            return (left + right) / 2
        return right if yright > yleft else left

    def LM(self, resolution=None):
        left, right = self.interval
        if self.__call__(left) < self.__call__(right):
            return right
        return left

    def RM(self, resolution=None):
        left, right = self.interval
        if self.__call__(left) > self.__call__(right):
            return left
        return right

    #endregion

    def __repr__(self):
        return 'Gamma({0}, {1}, {2})'.format(self.value, self.k, self.interval)

    __str__ = __repr__
