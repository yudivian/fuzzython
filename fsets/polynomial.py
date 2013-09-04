from fsets.fuzzy_set import FuzzySet

__author__ = ''


class Polynomial(FuzzySet):
    """
    Fuzzy Set with a polynomial function of membership
    :coefficients: is an enumerable of numbers
    (a, b, c) -> a*x^2 + b*x + c
    :interval: interval used for defuzzification
    """

    __slots__ = ('_coefficients', )

    def __init__(self, *coefficients, interval):
        if isinstance(interval, tuple):
            interval = Interval(*interval)
        super(Polynomial, self).__init__(None, interval)
        while len(coefficients) > 0 and coefficients[0] == 0:
            coefficients = coefficients[1:]
        self._coefficients = list(coefficients)

    def __call__(self, x):
        coefficients = self._coefficients
        if len(coefficients) == 0:
            return 0.0
        res = coefficients[-1]
        x_pow = x
        for c in coefficients[-2::-1]:
            res += c*x_pow
            x_pow *= x
        return res

    membership = __call__

    #region Function operations

    def __add__(self, other):
        if isinstance(other, Polynomial):
            c1 = self.get_coefficients(other.grade)
            c2 = other.get_coefficients(self.grade)
            coefficients = []
            for index in range(len(c1)):
                c = c1[index] + c2[index]
                coefficients.append(c)
            return Polynomial(*coefficients, interval=self.interval)
        if not callable(other):
            coefficients = self._coefficients[:] if self._coefficients else [0]
            coefficients[-1] += other
            return Polynomial(*coefficients, interval=self.interval)
        return super(Polynomial,self).__add__(other)

    __radd__ = __add__

    def __mul__(self, other):
        if isinstance(other, Polynomial):
            pol = Polynomial(interval=self.interval)
            length = len(self._coefficients)
            for i, c1 in enumerate(self._coefficients):
                coefficients = []
                for c2 in other._coefficients:
                    coefficients.append(c1*c2)
                coefficients += [0]*(length - 1 - i)
                pol = pol+Polynomial(*coefficients, interval=self.interval)
            return pol
        if not callable(other):
            return Polynomial(*map(lambda c: c*other, self._coefficients),
                              interval=self.interval)
        return super(Polynomial,self).__mul__(other)

    __rmul__ = __mul__

    def __sub__(self, other):
        if isinstance(other, Polynomial):
            c1 = self.get_coefficients(other.grade)
            c2 = other.get_coefficients(self.grade)
            coefficients = []
            for index in range(len(c1)):
                c = c1[index] - c2[index]
                coefficients.append(c)
            return Polynomial(*coefficients, interval=self.interval)
        if not callable(other):
            coefficients = self._coefficients[:] if self._coefficients else [0]
            coefficients[-1] -= other
            return Polynomial(*coefficients, interval=self.interval)
        return super(Polynomial,self).__sub__(other)

    def __rsub__(self, other):
        if isinstance(other, Polynomial):
            c1 = other.get_coefficients(self.grade)
            c2 = self.get_coefficients(other.grade)
            coefficients = []
            for index in range(len(c1)):
                c = c1[index] - c2[index]
                coefficients.append(c)
            return Polynomial(*coefficients, interval=self.interval)
        if not callable(other):
            coefficients = self._coefficients[:] if self._coefficients else [0]
            coefficients[-1] = other - coefficients[-1]
            return Polynomial(*coefficients, interval=self.interval)
        return super(Polynomial,self).__rsub__(other)

    def __truediv__(self, other):
        if not callable(other):
            coefficients = map(lambda c: c/other, self._coefficients)
            return Polynomial(*coefficients, interval=self.interval)
        return super(Polynomial,self).__truediv__(other)

    def __pow__(self, power, modulo=None):
        if isinstance(power, int):
            p = Polynomial(1, interval=self.interval)
            while power > 0:
                p = p*self
                power -= 1
            return p
        return super(Polynomial, self).__pow__(power, modulo)

    #endregion

    #region Function stuff

    def integral(self):
        """
        Gets the polynomial that represents the integral of current instance
        """
        coefficients = []
        length = len(self._coefficients)
        for i, c in enumerate(self._coefficients):
            power = length - i
            coefficients.append(c/power)
        coefficients.append(0)
        return Polynomial(*coefficients, interval=self.interval)

    def area(self, resolution=None):
        return self.area_(*self.interval)

    def area_(self, a, b):
        I = self.integral()
        return I(b) - I(a)

    @property
    def grade(self):
        """
        Polynomial grade
        """
        return len(self._coefficients)

    def get_coefficients(self, grade=None):
        if grade is None:
            return self._coefficients
        grade -= self.grade
        if grade <= 0:
            return self._coefficients
        return [0]*grade + self._coefficients

    def _remove_zeros(self):
        """
        Removes initials zeros from coefficients
        """
        while len(self._coefficients) > 0 and self._coefficients[0] == 0:
            self._coefficients = self._coefficients[1:]

    def __getitem__(self, item):
        return self._coefficients[item]

    def __setitem__(self, key, value):
        self._coefficients[key] = value
        self._remove_zeros()

    #endregion

    def __repr__(self):
        length = len(self._coefficients)
        if length == 0: return 'Polynomial: 0'

        def term_format(item):
            index, coefficient = item
            parenthesis = '()' if coefficient < 0 else ('','')
            power = length - 1 - index
            if power:
                return '{2}{0}{3}*X^{1}'.format(coefficient, power, *parenthesis)
            return '{1}{0}{2}'.format(coefficient, *parenthesis)

        s = map(term_format, enumerate(self._coefficients))
        return 'P(X): ' + ' + '.join(s)

    def __str__(self):
        return 'Polynomial(' + ','.join(self._coefficients)+'interval=({0},{1}))'.format(*self.interval)

