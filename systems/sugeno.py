from systems.system import System
from utils import timer

__author__ = ''

class SugenoSystem(System):
    """
    Represent a Sugeno model for fuzzy inference system
    """

    __slots__ = ()

    #@timer('[sugeno system time]')
    def inference(self):
        res = {}
        for ruleblock in self.blocks.values():
            we = [rule.compute() for rule in ruleblock.rules]
            # --- weighted average ---
            num = [firing_level*crisp for firing_level, crisp in we]
            den = [firing_level for firing_level, _ in we]
            try:
                res[ruleblock.name] = sum(num) / sum(den)
            except ZeroDivisionError:
                res[ruleblock.name] = 0
        return res

    @timer('[sugeno system time]')
    def compute(self, inputs, outputs=None):
        """
        Do a complete fuzzy calculation step
        :param inputs: dictionary with inputs values for variables
        :param outputs: not used
        """
        self.reset()
        self.fuzzify(inputs)
        return self.inference()

    def dump_type(self):
        return '_SUGENO_ '

    def __repr__(self):
        return 'Sugeno System with {0} block rules'.format(len(self.blocks))

    __str__ = __repr__
