from fsets.fuzzy_set import FuzzySet

__author__ = ''

class Variable:
    """
    Describes a variable
    """

    __slots__ = ('adjectives', 'name', 'unit', 'defuzzification', 'default', 'value', 'interval')

    def __init__(self, name, unit='', *adjectives, defuzzification=None, default=None, interval=None):
        """
        Initialize a variable
        :param name: variable name
        :param unit: variable unit
        :param adjectives: adjectives for this variable
        :param defuzzification: defuzzification method for output value of variable
        :param default: defuzzification value on error
        :param interval:
        """
        self.defuzzification = defuzzification
        self.adjectives = list(adjectives)
        self.name = name
        self.unit = unit
        self.default = default
        self.interval = interval
        self.value = None

    def reset(self):
        """
        Reset memberships of adjectives for new calculation step
        """
        for adjective in self.adjectives:
            adjective._strength = None
            adjective.set_ = None
        #self.value = None

    def fuzzify(self, value=None):
        self.value = value
        return [(adj, adj.membership(value)) for adj in self.adjectives]


    def defuzzify(self, accumulation=None):
        """
        Get the defuzzification value for this variable
        :param accumulation: accumulation method
        """
        try:
            defuzzification = self.defuzzification

            if defuzzification == 'COGS':
                from fsets.singleton import Singleton
                num, den = 0, 0
                for adjective in self.adjectives:
                    singleton = adjective.fset
                    if not isinstance(singleton, Singleton):
                        continue
                    strength = adjective.strength
                    num += singleton.x*strength
                    den += strength
                return num / den

            # accumulate adjective's fset...
            sets = [adjective.set_ for adjective in self.adjectives if adjective.set_]
            fuzzy_set = FuzzySet.disjunction(*sets, snorm=accumulation)

            attr = getattr(fuzzy_set, defuzzification)
            return attr()
        except Exception as e:
            print(e)
            return self.default

        #return self.default

    def __contains__(self, item):
        return item in self.adjectives

    def __float__(self):
        return float(self.value)

    #region Operators

    def __add__(self, other):
        return self.value + float(other)

    __radd__ = __add__

    def __mul__(self, other):
        return self.value * float(other)

    __rmul__ = __mul__

    def __sub__(self, other):
        return self.value - float(other)

    def __rsub__(self, other):
        return float(other) - self.value

    def __truediv__(self, other):
        return self.value / float(other)

    def __rtruediv__(self, other):
        return float(other) / self.value

    def __div__(self, other):
        return self.value // float(other)

    def __rdiv__(self, other):
        return float(other) // self.value

    #endregion

    #region Dump

    def var_declaration(self, prefix=''):
        return prefix + self.name + ':\t' + 'REAL;'

    def terms(self, prefix=''):
        s = ''
        for adjective in self.adjectives:
            s += prefix + 'TERM ' + adjective.name + ' := ' +\
                 str(adjective._fuzzy_set) + ';'
        return s

    def methods(self, prefix=''):
        s = prefix + 'METHOD:\t' + self.defuzzification + ';'
        d = self.default
        d = '' if d is None else prefix + 'DEFAULT := {0};'.format(d)
        return s + d

    #endregion

    def __repr__(self):
        value = ' = ' + repr(self.value) if self.value else ''
        return 'Variable {0}({1}){2}'.format(self.name, self.unit or '?', value)

    def __str__(self):
        return self.name

