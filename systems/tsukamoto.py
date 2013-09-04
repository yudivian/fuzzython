from systems.system import System
from utils import timer

__author__ = ''

class TsukamotoSystem(System):
    """
    Represent a Tsukamoto model for fuzzy inference system
    """

    __slots__ = ()

    #@timer('[tsukamoto system time]')
    def inference(self):
        res = {}
        for ruleblock in self.blocks.values():
            we = [rule.compute() for rule in ruleblock.rules]
            num = [firing_level*xi for firing_level, xi in we]
            den = [firing_level for firing_level, _ in we]
            try:
                # num, den = 0, 0
                # for wi, xi in we:
                #     num += wi*xi
                #     den += wi
                res[ruleblock.name] = sum(num) / sum(den)
            except ZeroDivisionError:
                res[ruleblock.name] = 0
        return res

    @timer('[tsukamoto system time]')
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
        return '_TSUKAMOTO_ '

    def __repr__(self):
        return 'Tsukamoto System with {0} block rules'.format(len(self.blocks))

    __str__ = __repr__
