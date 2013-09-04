from fsets.fuzzy_set import FuzzySet
from fsets.sfunction import SFunction
from fsets.zfunction import ZFunction
from interval import Interval

__author__ = ''

class PiFunction(FuzzySet):
    """
    Represents a fuzzy set with a Pi-shaped function
                _
               /|\
              / | \
            _/  |  \_
            | center|
            |   |   |
           delta delta
    """

    __slots__ = ('_center', '_delta', '_min_', '_max_')

    def __init__(self, center, delta, min_=0, max_=1):
        super(PiFunction, self).__init__(None, Interval(center-delta, center+delta))
        self._center = center
        self._delta = delta
        self._min_ = min_
        self._max_ = max_

    def __call__(self, x):
        center = self._center
        delta = self._delta
        if x <= center:
            return SFunction(center - delta, center - delta/2, center)(x)
        else:
            return ZFunction(center, center + delta/2, center + delta)(x)

    #region defuzzifying methods

    def COG(self, resolution=None):
        return self._center

    def COA(self, precision=0.0000001):
        return self._center

    def MM(self, resolution=None):
        return self._center

    def CM(self, resolution=None):
        return self._center

    def LM(self, resolution=None):
        return self._center

    def RM(self, resolution=None):
        return self._center

    #endregion

    def __repr__(self):
        return 'PiFunction({0},{1},{2},{3})'.format(self._center, self._delta, self._min_, self._max_)

    __str__ = __repr__
