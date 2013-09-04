from predicate import Predicate

__author__ = ''


class Rule(object):
    """
    Base class for fuzzy rules
    """

    __COUNT = 0

    __slots__ = ('_antecedent', '_consequent', '_weight', '_number')

    def __init__(self, antecedent, consequent, weight=1):
        """
        Initialize a rule
        :param antecedent: premise (if part)
        :param consequent: conclusion (then part)
        :param weight: how sure are we about this rule
        """
        self._antecedent = antecedent
        self._consequent = consequent
        self._weight = weight
        self._number = Rule.__COUNT
        Rule.__COUNT += 1

    def get_weight(self):
        return self._weight

    def set_weight(self, value):
        if 0 < value <= 1:
            self._weight = value

    weight = property(get_weight, set_weight, doc='weight factor')

    def compute(self, activation=None):
        """Compute rule's firing level and sets this value for adjectives in consequent"""
        pass

    #region (IN/OUT) Adjectives, Variables

    def input_adj(self):
        """
        Gets all adjectives in the antecedent of rule
        """
        antecedent = self._antecedent
        if isinstance(antecedent, Predicate):
            return [antecedent.adjective]
        return list({p.adective for p in antecedent.leaves()})

    def output_adj(self):
        """
        Gets all adjectives in the consequent of rule
        """
        return [predicate.adjective for predicate in self._consequent]

    def input_vars(self):
        """
        Gets all variables in the antecedent of rule
        """
        antecedent = self._antecedent
        if isinstance(antecedent, Predicate):
            return [antecedent.variable]
        return list({p.variable for p in antecedent.leaves()})

    def output_vars(self):
        """
        Gets all variables in the consequent of rule
        """
        return [predicate.variable for predicate in self._consequent]

    #endregion

    #region (IN/OUT) Predicates

    def inputs(self):
        """
        Gets all predicates in the antecedent of rule
        """
        antecedent = self._antecedent
        if isinstance(antecedent, Predicate):
            return [antecedent]
        return list({p for p in antecedent.leaves()})

    def outputs(self):
        """
        Gets all predicates in the consequent of rule
        """
        return [predicate for predicate in self._consequent]

    def predicates(self):
        """
        Gets all predicates in the rule
        """
        return self.inputs() + self.outputs()

    #endregion

    @staticmethod
    def parse(sentence, scope, tnorm=None, snorm=None, cnorm=None):
        """
        Parse a str-rule with given scope and norms
        """
        from rules.parser import parse_rule
        return parse_rule(sentence, scope, tnorm, snorm, cnorm)

    @staticmethod
    def get_rule(antecedent, consequent, weight=1):
        """
        Gets a correct rule for...
        :param antecedent: the structure of antecedent is an operator's tree of predicates
        :param consequent: the structure of consequent determines the rule type
        :param weight: certainty for this rule
        """
        if isinstance(consequent, list):
            from rules.mrule import MRule
            XRule = MRule
        elif isinstance(consequent, Predicate):
            from rules.trule import TRule
            XRule = TRule
        else:
            from rules.srule import SRule
            XRule = SRule
        return XRule(antecedent, consequent, weight)

    def __repr__(self):
        w = '' if self._weight == 1 else ' WITH ' + str(self._weight)
        if isinstance(self._consequent, list):
            consequent = ', '.join([str(predicate) for predicate in self._consequent])
        else:
            consequent = self._consequent
        return 'RULE {0}: IF {1} THEN {2}{3};'.format(self._number, self._antecedent, consequent, w)

    __str__ = __repr__
