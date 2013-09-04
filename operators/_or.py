from norms.norms import maximum
from operators.binary import Binary
from operators.operator import Operator

__author__ = ''

class Or(Binary):
    NORM = maximum

    def __init__(self, left, right, snorm=None):
        super(Or, self).__init__(left, right, snorm or Or.NORM)

    def __repr__(self):
        left, right = isinstance(self._left, Operator), isinstance(self._right, Operator)
        left = '({0})'.format(self._left) if left else self._left
        right = '({0})'.format(self._right) if right else self._right
        #return '({0}) OR ({1})'.format(self._left, self._right)
        return '{0} OR {1}'.format(left, right)

    __str__ = __repr__

