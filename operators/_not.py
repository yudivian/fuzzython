from norms.norms import zadeh_complement
from operators.unary import Unary

__author__ = ''

class Not(Unary):
    NORM = zadeh_complement

    def __init__(self, operand, norm=None):
        super(Not, self).__init__(operand, norm or Not.NORM)

    def __repr__(self):
        return 'NOT ({0})'.format(self._operand)

    __str__ = __repr__

