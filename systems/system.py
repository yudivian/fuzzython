from ruleblock import RuleBlock

__author__ = ''

class System(object):
    """
    Base class for fuzzy inference system
    Holds all stuff together (predicates, rules, ...)
    """

    __slots__ = ('name', 'blocks')

    def __init__(self, name, *blocks):
        """
        Initialize a fuzzy system
        :param name: system name
        :param blocks: blocks of rules
        """
        self.name = name
        # self.variables = {}
        self.blocks = {}
        self.add_blocks(*blocks)

    def add_blocks(self, *blocks):
        """
        Incorporate the block of rules in the system
        :param blocks: list of rule-block
        """
        for block in blocks:
            assert isinstance(block,RuleBlock), 'error type in block {}'.format(block)
            self.blocks[block.name] = block

    #region IN/OUT Variables

    def input_variables(self):
        """Get the inputs variables"""
        variables = {}
        for ruleblock in self.blocks.values():
            variables.update(ruleblock.inputs.items())
        return variables

    def output_variables(self):
        """Get the outputs variables"""
        variables = {}
        for ruleblock in self.blocks.values():
            variables.update(ruleblock.outputs.items())
        return variables

    #endregion

    #@timer('[system time]')
    def reset(self):
        """Reset all memberships for the next run of calculate"""
        for block in self.blocks.values():
            block.reset()

    #@timer('[system time]')
    def fuzzify(self, inputs):
        """
        Fuzzify the inputs
        :param inputs: dictionary with inputs values for variables
        """
        for block in self.blocks.values():
            block.fuzzify(inputs)

    def inference(self):
        """Calculate the fuzzy inference given by the rules"""
        pass

    def compute(self, inputs, outputs=None):
        """
        Do a complete fuzzy calculation step
        :param inputs: dictionary with inputs values for variables
        :param outputs: dictionary with variables to read
        """
        pass

    #region FCL Representation

    def dump(self, filename):
        """
        Save to FCL-E the current fuzzy system
        :param filename: file path
        """
        #s = '\n(* FCL *)\n'
        with open(filename, 'w') as file:
            file.write('\n')
            file.write(self.dump_())
            file.write('\n')

    def dump_(self):
        type_ = self.dump_type()
        s = 'FUNCTION_BLOCK {0}'.format(type_) + self.name

        # INPUTS - OUTPUTS
        for variable in self.input_variables().values():
            s += '\n\tVAR_INPUT\n' + variable.var_declaration('\t\t') + \
                 '\n\tEND_VAR'
        for variable in self.output_variables().values():
            s += '\n\tVAR_OUTPUT\n' + variable.var_declaration('\t\t') + \
                 '\n\tEND_VAR'

        #FUZZIFY - DEFUZZIFY
        for variable in self.input_variables().values():
            s += '\n\tFUZZIFY ' + variable.name \
                 + variable.terms('\n\t\t') + \
                 '\n\tEND_FUZZIFY'
        for variable in self.output_variables().values():
            s += '\n\tDEFUZZIFY ' + variable.name \
                 + variable.terms('\n\t\t') + \
                 variable.methods('\n\t\t') + \
                 '\n\tEND_DEFUZZIFY'

        #RULE BLOCKS
        for ruleblock in self.blocks.values():
            s += '\n' + ruleblock.dump('\t')

        return s + '\nEND_FUNCTION_BLOCK'

    def dump_type(self):
        """Get the system type"""
        return ''

    #endregion

    def __repr__(self):
        return 'System'

    __str__ = __repr__


