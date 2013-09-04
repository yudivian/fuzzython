from fsets.fuzzy_set import FuzzySet

__author__ = ''

class Adjective(object):
    """
    Describes a variable

    :_fuzzy_set: fuzzy set from module fsets
    :name: adjective's name
    :_strength: computed firing level
    :set_: modified fuzzy set corresponding to strength value
    """

    __slots__ = ('_fuzzy_set', '_name', '_strength', 'set_')

    def __init__(self, name, fuzzy_set):
        """
        Initialize adjective

        :param name: adjective's name
        :param fuzzy_set: fuzzy set
        """
        self._fuzzy_set = fuzzy_set
        self._name = name
        self._strength = None
        self.set_ = None

    def membership(self,  value):
        """
        Get membership for an input value

        :param value: crisp value or fuzzy set
        """
        if isinstance(value, FuzzySet):
            return self._fuzzy_set.fuzzify_with(value)
            #value = value.intersect(self._fuzzy_set)
            #return value(value.LM())
        return self._fuzzy_set(value)

    #region Properties

    @property
    def fset(self):
        return self._fuzzy_set

    @property
    def name(self):
        return self._name

    def get_strength(self):
        return self._strength or 0.0

    def set_strength(self, value):
        if self._strength:
            self._strength = max(self._strength, value)
        else:
            self._strength = value

    strength = property(get_strength, set_strength, doc='computed firing level')

    #endregion

    #region Adjective modifiers

    def _adjective_(self, norm, value):
        """
        Get new adjective with same name modifying fuzzy set

        :param norm: function norm from norms
        :param value: crisp value
        """
        return Adjective(self._name, self._fuzzy_set.activate(norm, value))

    def _set_(self, norm):
        """
        Set the corresponding fuzzy set for previous calculated strength using the given norm

        :param norm: function norm from norms
        """
        value = self._strength
        if value > 0:
            self.set_ = self._fuzzy_set.activate(norm, value)
        else:
            self.set_ = None

    #endregion

    def __repr__(self):
        return 'Adjective {0}:{1}'.format(self._name, self._fuzzy_set)

    def __str__(self):
        return self._name
