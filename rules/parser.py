from predicate import Predicate

__author__ = ''


IS, AND, OR, NOT, IF, THEN, WITH, EQUAL = 'is', 'and', 'or', 'not', 'if', ' then ', 'with', '='
OPEN_PAR, CLOSE_PAR = '(', ')'
RULE_TYPES = 'mamdani', 'sugeno'


def parse_rule(sentence, scope, tnorm, snorm, cnorm):
    """
    Parse a if-then string rule with variables and adjectives in scope dictionary
    :param sentence: if-then rule with (mamdani/sugeno/tsukamoto) format
    :param scope: scope dictionary use for parsing task
    :param tnorm: norm use for and operator
    :param snorm: norm use for or operator
    :param cnorm: norm use for not operator
    """
    assert isinstance(sentence, str), 'sentence must be a string'

    from operators.operator import Operator

    if ':' in sentence:
        system_type , sentence, *empty_list = sentence.split(':')
    else:
        system_type = None

    if_, then_ = sentence.split(THEN)
    index = if_.index(IF)
    if_ = if_[index+len(IF):]
    antecedent = Operator.build_tree(if_, scope, tnorm, snorm, cnorm)

    # or (EQUAL in then_ and not WITH in then_)
    if system_type == 's' or (not IS in then_): # Sugeno Consequent
        from rules.srule import SRule
        index = then_.index(EQUAL)
        consequent = then_[index+1:]
        if WITH in consequent:
            consequent, weight, *rest = consequent.split(WITH)
            weight = float(weight.strip())
        else:
            weight = 1
        consequent = consequent.strip()
        rule = SRule(antecedent, consequent, weight)
    else:  # Mamdani Consequent... predicate
        then_ = then_.replace(',', ' , ')
        then_ = then_.rstrip(';')
        consequent, weight = _conclusion(then_.split(), scope)
        if system_type == 't':
            from rules.trule import TRule
            return TRule(antecedent, consequent[0], weight)
        from rules.mrule import MRule
        rule = MRule(antecedent, consequent, weight)

    return rule


def _conclusion(consequent, scope):
    """
    Gets a rule consequent (then part of a rule)
    """
    predicates = []
    weight = 1
    length = len(consequent)
    index = 0

    while index < length:
        predicate, size = _predicate(consequent, index, scope, accept_negation=False)
        index += size
        eof = index >= length
        if not eof and consequent[index] == WITH:
            index += 1
            weighting_factor = consequent[index]
            index += 1
            weight = float(weighting_factor)

        predicates.append(predicate)
        index += 1 # ','

    return predicates, weight

def _predicate(antecedent, index, scope, accept_negation=True):
    """
    Gets a predicate (variable is adjective)
    :param antecedent: if-part or then-part of a string-rule
    :param index: index of string to parse
    :param scope: scope dictionary
    :param accept_negation: True if we allow variable is NOT adjective
    """
    initial_pos = index
    var = antecedent[index]
    index+=1
    assert antecedent[index] == IS, "expected 'is' word"
    index+=1

    negate = antecedent[index] == NOT
    if not accept_negation and negate:
        raise Exception("predicate can't negate")

    if negate: index+=1

    adj = antecedent[index]
    index+=1

    var, adj = scope.get(var), scope.get(adj)

    if not (var and adj):
        raise Exception('predicate sentence not well formed')

    predicate = Predicate(var, adj)
    return predicate, index - initial_pos
