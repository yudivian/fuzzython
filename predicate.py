
__author__ = ''

class Predicate(object):
    """
    Fuzzy Predicate is represented as 'variable is adjective'

    :variable: fuzzy variable
    :adjective: fuzzy adjective
    """

    __slots__ = ('adjective', 'variable')

    def __init__(self, variable, adjective):
        """
        Initialize predicate

        :param variable: fuzzython.variable
        :param adjective: fuzzython.adjective
        """
        self.adjective = adjective
        self.variable = variable
        #self._weight = weight


    def evaluate(self):
        """
        Gets a value of how much apply the adjective to variable
        """
        return self.adjective.membership(self.variable.value)

    def change_predicate(self, norm, value):
        adjective = self.adjective._adjective_(norm, value)
        return Predicate(self.variable, adjective)

    def __contains__(self, item):
        return item == self.variable or item == self.adjective

    def __iter__(self):
        yield from (self.variable, self.adjective)

    def __repr__(self):
        return '{0} IS {1}'.format(self.variable, self.adjective)

    __str__ = __repr__


