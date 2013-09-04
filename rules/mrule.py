from rules.rule import Rule

__author__ = ''


class MRule(Rule):
    """
    Represent a Mamdani Rule (using minimum norm for activation)
    Activation method may vary between several tnorms
    Larsen Rule (activation is performed with product)
    """

    __slots__ = ()

    def __init__(self, antecedent, consequent, weight=1):
        super(MRule, self).__init__(antecedent, consequent, weight)

    def compute(self, activation=None):
        strength = self._antecedent.evaluate()*self._weight

        if activation is not None: # minimum or product
            for predicate in self._consequent:
                predicate.adjective.strength = strength #*predicate.weight
                predicate.adjective._set_(activation)
        else:
            for predicate in self._consequent:
                predicate.adjective.strength = strength #*predicate.weight

    def __repr__(self):
        return 'MRule {0}: IF {1} THEN {2}'.format(self._number, repr(self._antecedent), self._consequent)

