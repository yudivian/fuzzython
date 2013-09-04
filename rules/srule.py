from rules.rule import Rule

__author__ = ''

class SRule(Rule):
    """
    Represent a Sugeno Rule (TSK Rule)
    Consequent is a function of inputs variables
    """

    __slots__ = ('_inputs', )

    def __init__(self, antecedent, consequent, weight=1):
        super(SRule, self).__init__(antecedent, consequent, weight)
        self._inputs = {variable.name:variable for variable in self.input_vars()}

    def outputs(self):
        return []

    def output_vars(self):
        return []

    def output_adj(self):
        return []

    def compute(self, activation=None):
        strength = self._antecedent.evaluate()*self._weight
        return strength, strength and eval(self._consequent, self._inputs)

    def crisp(self):
        return eval(self._consequent, self._inputs)

    def __repr__(self):
        return 'SRule {0}: IF {1} then {2}'.format(self._number, repr(self._antecedent), self._consequent)
