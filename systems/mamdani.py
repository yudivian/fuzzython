from systems.system import System
from utils import timer

__author__ = ''

class MamdaniSystem(System):
    """
    Represent a Mamdani model for fuzzy inference system
    """

    __slots__ = ()

    #@timer('[mamdani system time]')
    def inference(self):
        for ruleblock in self.blocks.values():
            activation = ruleblock.activation
            for rule in ruleblock.rules:
                rule.compute(activation)

    #@timer('[mamdani system time]')
    def defuzzify(self, outputs=None):
        """
        Defuzzify the outputs variables
        :param outputs: dictionary with outputs variables
        """
        res = {}
        for ruleblock in self.blocks.values():
            outs = outputs or ruleblock.outputs
            acc = ruleblock.accumulation
            v = {name:var.defuzzify(acc) for name,var in outs.items()}
            res[ruleblock.name] = v
        return res

    @timer('[mamdani system time]')
    def compute(self, inputs, outputs=None):
        self.reset()
        self.fuzzify(inputs)
        self.inference()
        return self.defuzzify(outputs)

    def __repr__(self):
        return 'Mamdani System with {0} block rules'.format(len(self.blocks))

    __str__ = __repr__
