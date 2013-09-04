from operators.operator import Operator

__author__ = ''

class Binary(Operator):
    """
    Binary Operator (AND, OR)
    """

    def __init__(self, left, right, norm):
        """
        Initialize a binary operator
        :param left: left operand
        :param right: right operand
        :param norm: function-norm to operate
        """
        self._right = right
        self._left = left
        self._norm = norm

    #region Properties

    def get_right(self):
        return self._right
    def set_right(self, value):
        self._right = value

    right = property(get_right, set_right, doc='right operand')

    def get_left(self):
        return self._left
    def set_left(self, value):
        self._left = value

    left = property(get_left, set_left, doc='left operand')

    #endregion

    def evaluate(self):
        left, right = self._left.evaluate(), self._right.evaluate()
        return self._norm(left, right)

    def print_tree(self, prefix=''):
        print('{0}{1}'.format(prefix, self))
        if isinstance(self._left, Operator):
            self._left.print_tree(prefix + '\t')
        else:
            print('\t{0}{1}'.format(prefix, self._left))
        if isinstance(self._right, Operator):
            self._right.print_tree(prefix + '\t')
        else:
            print('\t{0}{1}'.format(prefix, self._right))

    def operands(self):
        return self._left, self._right

    def __repr__(self):
        return 'Binary Operator'

    __str__ = __repr__

