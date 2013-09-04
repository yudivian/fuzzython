from norms.norms import get_norm
from rules.rule import Rule

__author__ = ''


class RuleBlock(object):
    """
    Represent a group of several rules with same accumulation, activation and operators definitions
    Each rule on the block shares the definitions for:
    tnorm, snorm, cnorm, and activation and accumulation methods
    """

    __slots__ = ('accumulation', 'activation', 'name', 'rules', 'outputs', 'inputs', 'and_', 'or_', 'not_')

    def __init__(self, name, operators=('MIN', 'MAX', 'ZADEH'), activation='MIN', accumulation='MAX'):
        """
        Initialize a block of rules
        :param name: rule-block name
        :param operators: definitions for 'and', 'or' and 'not' operators
        :param activation: definition of activation method
        :param accumulation: definition of accumulation method
        """
        self.accumulation = get_norm(accumulation)
        self.activation = get_norm(activation)
        self.set_operators(operators)
        self.name = name
        self.inputs = {}
        self.outputs = {}
        self.rules = []

    def set_operators(self, operators):
        """Set the function norms used for 'and', 'or' and 'not' operators"""
        and_, or_, not_ = operators
        self.and_ = get_norm(and_ or 'MIN')
        self.or_ = get_norm(or_ or 'MAX')
        self.not_ = get_norm(not_ or 'ZADEH')

    def addrule(self, rule):
        """
        Append rule to the block's rules
        :param rule: Any rule instance from rules package
        """
        for var in rule.input_vars():
            self.inputs[var.name] = var
        for var in rule.output_vars():
            self.outputs[var.name] = var

        self.rules.append(rule)
        pass

    def add_rule(self, rule, scope):
        """
        Parse and append rule to the block's rules
        :param rule: str-rule (string of the form 'if var1 is adj1 then var2 is adj2')
        :param scope: scope with variables and adjectives to parse the string
        """
        rule = Rule.parse(rule, scope, self.and_, self.or_, self.not_)

        for var in rule.input_vars():
            self.inputs[var.name] = var
        for var in rule.output_vars():
            self.outputs[var.name] = var

        self.rules.append(rule)

    def add_rules(self, *rules, scope):
        for rule in rules:
            self.add_rule(rule, scope)

    #@timer('[rule block time]')
    def reset(self):
        """
        Reset variables for next inference process
        """
        for variable in self.inputs.values():
            variable.reset()
        for variable in self.outputs.values():
            variable.reset()

    #@timer('[rule block time]')
    def fuzzify(self, inputs):
        """
        Fuzzify the variables with values given in inputs
        :param inputs: dictionary with values for input variables
        """
        for var_name, value in inputs.items():
            if var_name in self.inputs:
                self.inputs[var_name].value = value
            else:
                print('not used input:', var_name)


    #region Dump

    def dump(self, prefix=''):
        prefix_ = '\n' + prefix + '\t'
        s = self.name + prefix_ +'AND: ' + self.and_.name + ';' + \
            prefix_ + 'ACT: ' + self.activation.name + ';' + \
            prefix_ + 'ACCU: ' + self.accumulation.name + ';' + \
            prefix_

        r = prefix_.join([str(rule) for rule in self.rules])

        return prefix + 'RULEBLOCK ' +  s + r + '\n' +\
               prefix + 'END_RULEBLOCK'

    #endregion

    def __iter__(self):
        yield from self.rules

    def __repr__(self):
        return 'Rule Block {0} with {1} rules'.format(self.name, len(self.rules))

    __str__ = __repr__
