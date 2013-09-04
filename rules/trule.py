from rules.rule import Rule

__author__ = ''


class TRule(Rule):
    """
    Represent a Tsukamoto Rule
    """

    __slots__ = ()

    def __init__(self, antecedent, consequent, weight=1):
        super(TRule, self).__init__(antecedent, consequent, weight)

    def compute(self, activation=None):
        strength = self._antecedent.evaluate()*self._weight
        return self.get_strength_x(self._consequent.adjective._fuzzy_set, strength)

    def get_x(self, fuzzyset, y, precision=0.0000001):
        """
        Gets a x-value in the fuzzy set which degree of membership is y
        :param fuzzyset: fuzzy set with a monotonic
        :param y: degree of membership
        :param precision: use for equality compare
        """
        a, b = fuzzyset.interval
        ya, yb = fuzzyset(a), fuzzyset(b)
        if y == ya: return a
        if y == yb: return b
        growing = ya <= yb
        c = (a + b) / 2
        y_ = fuzzyset(c)
        if growing:
            if y < ya or yb < y:
                return None
            while abs(y - y_) > precision:
                if y_ > y:
                    b = c
                elif y_ < y:
                    a = c
                else:
                    return c
                c = (a + b) / 2
                y_ = fuzzyset(c)
        else:
            if y < yb or ya < y:
                return None
            while abs(y - y_) > precision:
                if y_ > y:
                    a = c
                elif y_ < y:
                    b = c
                else:
                    return c
                c = (a + b) / 2
                y_ = fuzzyset(c)
        return c

    def get_strength_x(self, fuzzyset, y, precision=0.0000001):
        a, b = fuzzyset.interval
        ya, yb = fuzzyset(a), fuzzyset(b)
        if y == ya: return y, a
        if y == yb: return y, b
        growing = ya <= yb
        c = (a + b) / 2
        y_ = fuzzyset(c)
        if growing:
            if y < ya or yb < y:
                return 0, 0 #None
            while abs(y - y_) > precision:
                if y_ > y:
                    b = c
                elif y_ < y:
                    a = c
                else:
                    return y, c
                c = (a + b) / 2
                y_ = fuzzyset(c)
        else:
            if y < yb or ya < y:
                return 0,0 #None
            while abs(y - y_) > precision:
                if y_ > y:
                    a = c
                elif y_ < y:
                    b = c
                else:
                    return y, c
                c = (a + b) / 2
                y_ = fuzzyset(c)
        return y, c

    def outputs(self):
        return [self._consequent]

    def output_vars(self):
        return [self._consequent.variable]

    def output_adj(self):
        return [self._consequent.adjective]

    def __repr__(self):
        return 'TRule {0}: {1} then {2}'.format(self._number, repr(self._antecedent), self._consequent)
