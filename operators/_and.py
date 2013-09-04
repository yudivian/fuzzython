from norms.norms import minimum
from operators.binary import Binary
from operators.operator import Operator

__author__ = ''

class And(Binary):

    NORM = minimum

    def __init__(self, left, right, tnorm=None):
        super(And, self).__init__(left, right, tnorm or And.NORM)

    def __repr__(self):
        left, right = isinstance(self._left, Operator), isinstance(self._right, Operator)
        left = '({0})'.format(self._left) if left else self._left
        right = '({0})'.format(self._right) if right else self._right
        return '{0} AND {1}'.format(left, right)

    __str__ = __repr__

