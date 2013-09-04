from operators.operator import Operator

__author__ = ''

class Unary(Operator):
    """
    Represent  unary operator
    """

    __slots__ = ('_operand', '_norm')

    def __init__(self, operand, norm):
        """
        Initialize an unary operator
        :param operand: single operand
        :param norm: function-norm to operate
        """
        self._operand = operand
        self._norm = norm

    def get_child(self):
        return self._operand

    def set_child(self, value):
        self._operand = value

    child = property(get_child, set_child, doc='child operand')

    def evaluate(self):
        return self._norm(self._operand.evaluate())

    def print_tree(self, prefix=''):
        print('{0}{1}'.format(prefix, self))
        if isinstance(self._operand, Operator):
            self._operand.print_tree(prefix + '\t')
        else:
            print('\t{0}{1}'.format(prefix, self._operand))

    def operands(self):
        return self._operand,
