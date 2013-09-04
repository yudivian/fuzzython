
__author__ = ''


class Operator(object):
    """
    Base class for any valid operator between fuzzy predicates
    """

    @staticmethod
    def build_tree(sentence, scope, tnorm=None, snorm=None, cnorm=None):
        """
        Creates a tree with operators (one of And, Or, Not) on each internal node
        and predicates on each leaf (node with no child)

        :param sentence: str-formatted expression like var1 is adj1 and var2 is adj2
        :param scope: dictionary to map names on sentence with real variables
        :param tnorm: norm used for intersection
        :param snorm: norm used for union
        """
        from operators.parser import Parser
        parser = Parser(sentence, scope, tnorm, snorm, cnorm)
        return parser.parse()

    def print_tree(self, prefix=''):
        """
        Represent operator's tree with custom format
        :param prefix: str used to indent each new tree-level
        """
        pass

    def evaluate(self):
        """
        Evaluate the operation's tree
        """
        pass

    def operands(self):
        """
        Gets the operands of current operator
        """
        pass

    def leaves(self):
        """
        Gets a list of predicates (leaf nodes)
        """
        res = []
        for operand in self.operands():
            if isinstance(operand, Operator):
                res += operand.leaves()
            else:
                res.append(operand)
        return res

    def __repr__(self):
        return 'Operator'

    __str__ = __repr__

