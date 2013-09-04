from adjective import Adjective
from operators._and import And
from operators._not import Not
from operators._or import Or
from predicate import Predicate
from variable import Variable

__author__ = ''


class Parser(object):
    """
    This class parse a string with predicates and operands formatted as follows:
    'var1 is adj1 and var2 is adj2 or var3 is adj3'
    ...and creates corresponding operators-tree

    Expr  -> Term Expr'
    Expr' -> 'or' Expr | epsilon
    Term  -> [predicate | '(' Expr ')' | 'not' '(' Expr ')'] Term'
    Term' -> 'and' Term | epsilon
    """

    IS, AND, OR, NOT, WITH = 'IS', 'AND', 'OR', 'NOT', 'WITH'
    OPEN_PAR, CLOSE_PAR = '(', ')'

    def __init__(self, sentence, scope, tnorm, snorm, cnorm):
        assert isinstance(sentence, str)
        if '(' in sentence:
            sentence = sentence.replace('(', ' ( ').replace(')', ' ) ')
        self.sentence = sentence.split()
        self.scope = scope or globals()
        self.index = -1
        self.snorm = snorm
        self.tnorm = tnorm
        self.cnorm = cnorm

    def parse(self):
        self.index = 0
        return self._expr()

    def _expr(self):
        #print('expr -> term expr_')
        term = self._term()
        exp_ = self._expr_()
        if exp_ is not None:
            return Or(term, exp_, self.snorm)
        return term

    def _expr_(self):
        #print('expr_ -> or expr | epsilon', end='\t::\t')
        eof = self.index >= len(self.sentence)
        if not eof and self.sentence[self.index].upper() == Parser.OR:
            #print('expr_ -> or expr')
            self.index+=1
            return self._expr()
        else:
            #print('expr_ -> epsilon')
            return None

    def _term(self, ancestor=None):
        #print('term -> predicate term_ | ( expr ) term_ | not ( expr )', end='\t::\t')
        if self.sentence[self.index] == Parser.OPEN_PAR:
            #print('term -> ( expr ) term_')
            self.index+=1
            expr = self._expr()
            assert self.sentence[self.index] == Parser.CLOSE_PAR, "expected ')'"
            self.index+=1
        elif self.sentence[self.index] == Parser.NOT:
            #print('term -> not ( expr ) term_')
            self.index+=1
            assert self.sentence[self.index] == Parser.OPEN_PAR, "expected '('"
            self.index+=1
            expr = self._expr()
            assert self.sentence[self.index] == Parser.CLOSE_PAR, "expected ')'"
            self.index+=1
            expr = Not(expr, self.cnorm)
        else:
            #print('term -> predicate term_')
            expr = self._predicate()

        if ancestor is not None:
            node = And(ancestor, expr, self.tnorm)
            follow = self._term_(node)
            return follow or node

        term_ = self._term_(expr)
        return term_ or expr

    def _term_(self, ancestor=None):
        #print('term_ -> and term | epsilon', end='\t::\t')
        eof = self.index >= len(self.sentence)
        if not eof and self.sentence[self.index].upper() == Parser.AND:
            #print('term_ -> and term')
            self.index+=1
            return self._term(ancestor)
            #return And(ancestor, term) #None, term
        else:
            #print('term_ -> epsilon')
            return None

    def _predicate(self): #  accept_negation=True
        sentence = self.sentence
        var = sentence[self.index]
        self.index+=1
        assert sentence[self.index].upper() == Parser.IS, "expected 'is' word"
        self.index+=1

        negate = sentence[self.index].upper() == Parser.NOT
        #f not accept_negation and negate:
        #    raise Exception("predicate can't negate")

        if negate: self.index+=1

        adj = sentence[self.index]
        self.index+=1

        if var not in self.scope or adj not in self.scope:
            raise Exception('predicate sentence not well formed')

        var, adj = self.scope[var], self.scope[adj]

        if not isinstance(var, Variable):
            raise Exception('{0} must be a Variable'.format(var))
        if not isinstance(adj, Adjective):
            raise Exception('{0} must be an Adjective'.format(adj))

        predicate = Predicate(var, adj)
        return Not(predicate, self.cnorm) if negate else predicate

    def __repr__(self):
        return 'Operator Parser'

    __str__ = __repr__


    def __repr__(self):
        return 'Parser {0}'.format(self.sentence)
