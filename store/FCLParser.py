# $ANTLR 3.5 C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g 2013-06-21 00:01:51

import sys
from antlr3 import *


#!/usr/bin/python3

from adjective import Adjective
from fsets import polygon, singleton
from interval import Interval
from operators._and import And
from operators._not import Not
from operators._or import Or
#from norms.norms import maximum, minimum
from predicate import Predicate
from ruleblock import RuleBlock
from rules.rule import Rule
from variable import Variable

#region variables and functions...

#op_norms = { 'AND':minimum, 'OR':maximum }

def get_system(name, type_=None):
	"""Get an instance of a system model
	:param name: system name
	:param type_: system type
	"""
	if type_ == '_SUGENO_':
		from systems.sugeno import SugenoSystem
		return SugenoSystem(name)
	elif type_ == '_TSUKAMOTO_':
		from systems.tsukamoto import TsukamotoSystem
		return TsukamotoSystem(name)
	from systems.mamdani import MamdaniSystem
	return MamdaniSystem(name)
	
def get_fset(name, params=None):
	"""Get an instance of a FuzzySet with a given name and params
	:param name: name of fuzzy set class in package fsets
	:param params: parameters for fuzzy set
	"""
	name_ = name.lower()
	module = __import__('fsets.'+name_, fromlist=(name,))
	class_ = module.__dict__[name]
	params = params or []
	fset = class_(*params)
	return fset

_oppairs = [('MIN', 'MAX'), ('PROD', 'ASUM'), ('BDIF', 'BSUM'), ('DPROD', 'DSUM'), ('EPROD', 'ESUM'), ('FAND', 'FOR')]

def check_op(operators):
	"""Complete operators definition
	"""
	and_, or_, not_ = operators
	if and_ and or_:
		return (and_, or_, not_ or 'ZADEH')
	ands = {x:y for x,y in _oppairs}
	if and_ in ands: # {'MIN', 'PROD', 'BDIF'}:
		return (and_, ands.get(and_), not_ or 'ZADEH')
	ors = {y:x for x,y in _oppairs}
	if or_ in ors: # {'MAX', 'ASUM', 'BSUM'}:
		return (ors.get(or_), or_, not_ or 'ZADEH')
	return (and_ or 'MIN', or_ or 'MAX', not_ or 'ZADEH')

#endregion




# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
T__14=14
T__15=15
T__16=16
T__17=17
T__18=18
T__19=19
T__20=20
T__21=21
T__22=22
T__23=23
T__24=24
T__25=25
T__26=26
T__27=27
T__28=28
T__29=29
T__30=30
T__31=31
T__32=32
T__33=33
T__34=34
T__35=35
T__36=36
T__37=37
T__38=38
T__39=39
T__40=40
T__41=41
T__42=42
T__43=43
T__44=44
T__45=45
T__46=46
T__47=47
T__48=48
T__49=49
T__50=50
T__51=51
T__52=52
T__53=53
T__54=54
T__55=55
T__56=56
COMMENT=4
DIGIT=5
EXPONENT=6
FLOAT=7
IDENTIFIER=8
INTEGRAL_LITERAL=9
LETTER=10
LETTER_=11
REAL_LITERAL=12
WS=13

# token names
tokenNamesMap = {
    0: "<invalid>", 1: "<EOR>", 2: "<DOWN>", 3: "<UP>",
    -1: "EOF", 14: "T__14", 15: "T__15", 16: "T__16", 17: "T__17", 18: "T__18", 
    19: "T__19", 20: "T__20", 21: "T__21", 22: "T__22", 23: "T__23", 24: "T__24", 
    25: "T__25", 26: "T__26", 27: "T__27", 28: "T__28", 29: "T__29", 30: "T__30", 
    31: "T__31", 32: "T__32", 33: "T__33", 34: "T__34", 35: "T__35", 36: "T__36", 
    37: "T__37", 38: "T__38", 39: "T__39", 40: "T__40", 41: "T__41", 42: "T__42", 
    43: "T__43", 44: "T__44", 45: "T__45", 46: "T__46", 47: "T__47", 48: "T__48", 
    49: "T__49", 50: "T__50", 51: "T__51", 52: "T__52", 53: "T__53", 54: "T__54", 
    55: "T__55", 56: "T__56", 4: "COMMENT", 5: "DIGIT", 6: "EXPONENT", 7: "FLOAT", 
    8: "IDENTIFIER", 9: "INTEGRAL_LITERAL", 10: "LETTER", 11: "LETTER_", 
    12: "REAL_LITERAL", 13: "WS"
}
Token.registerTokenNamesMap(tokenNamesMap)

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>",
    "COMMENT", "DIGIT", "EXPONENT", "FLOAT", "IDENTIFIER", "INTEGRAL_LITERAL", 
    "LETTER", "LETTER_", "REAL_LITERAL", "WS", "'('", "')'", "'*'", "'+'", 
    "','", "'-'", "'.'", "'..'", "'/'", "':'", "';'", "'='", "'ACCU'", "'ACT'", 
    "'AND'", "'DEFAULT'", "'DEFUZZIFY'", "'END_DEFUZZIFY'", "'END_FUNCTION_BLOCK'", 
    "'END_FUZZIFY'", "'END_RULEBLOCK'", "'END_VAR'", "'FUNCTION_BLOCK'", 
    "'FUZZIFY'", "'IF'", "'IS'", "'METHOD'", "'NC'", "'NOT'", "'OR'", "'RANGE'", 
    "'REAL'", "'RETAIN'", "'RULE'", "'RULEBLOCK'", "'TERM'", "'THEN'", "'VAR_INPUT'", 
    "'VAR_OUTPUT'", "'WITH'", "'_MAMDAMI_'", "'_SUGENO_'", "'_TSUKAMOTO_'"
]



class FCLParser(Parser):
    grammarFileName = "C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g"
    api_version = 1
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super().__init__(input, state, *args, **kwargs)




        self.system = None
        self.scope = {}


        self.delegates = []





    class function_block_type_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()






    # $ANTLR start "function_block_type"
    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:86:1: function_block_type : ( '_MAMDAMI_' | '_SUGENO_' | '_TSUKAMOTO_' );
    def function_block_type(self, ):
        retval = self.function_block_type_return()
        retval.start = self.input.LT(1)


        try:
            try:
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:87:2: ( '_MAMDAMI_' | '_SUGENO_' | '_TSUKAMOTO_' )
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:
                pass 
                if self.input.LA(1) in {54, 55, 56}:
                    self.input.consume()
                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "function_block_type"



    # $ANTLR start "function_block_declaration"
    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:89:1: function_block_declaration : 'FUNCTION_BLOCK' ( function_block_type )? name= IDENTIFIER ( fb_io_var_declarations )* function_block_body 'END_FUNCTION_BLOCK' EOF ;
    def function_block_declaration(self, ):
        name = None
        function_block_type1 = None

        try:
            try:
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:90:2: ( 'FUNCTION_BLOCK' ( function_block_type )? name= IDENTIFIER ( fb_io_var_declarations )* function_block_body 'END_FUNCTION_BLOCK' EOF )
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:90:4: 'FUNCTION_BLOCK' ( function_block_type )? name= IDENTIFIER ( fb_io_var_declarations )* function_block_body 'END_FUNCTION_BLOCK' EOF
                pass 
                self.match(self.input, 36, self.FOLLOW_36_in_function_block_declaration66)

                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:90:21: ( function_block_type )?
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if (LA1_0 in {54, 55, 56}) :
                    alt1 = 1
                if alt1 == 1:
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:90:21: function_block_type
                    pass 
                    self._state.following.append(self.FOLLOW_function_block_type_in_function_block_declaration68)
                    function_block_type1 = self.function_block_type()

                    self._state.following.pop()




                name = self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_function_block_declaration73)

                #action start
                self.system = get_system(name.text, ((function_block_type1 is not None) and [self.input.toString(function_block_type1.start,function_block_type1.stop)] or [None])[0])
                #action end


                #action start
                self.type_ = ((function_block_type1 is not None) and [self.input.toString(function_block_type1.start,function_block_type1.stop)] or [None])[0]
                #action end


                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:93:3: ( fb_io_var_declarations )*
                while True: #loop2
                    alt2 = 2
                    LA2_0 = self.input.LA(1)

                    if (LA2_0 in {51, 52}) :
                        alt2 = 1


                    if alt2 == 1:
                        # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:93:3: fb_io_var_declarations
                        pass 
                        self._state.following.append(self.FOLLOW_fb_io_var_declarations_in_function_block_declaration85)
                        self.fb_io_var_declarations()

                        self._state.following.pop()


                    else:
                        break #loop2


                self._state.following.append(self.FOLLOW_function_block_body_in_function_block_declaration99)
                self.function_block_body()

                self._state.following.pop()

                self.match(self.input, 32, self.FOLLOW_32_in_function_block_declaration106)

                self.match(self.input, EOF, self.FOLLOW_EOF_in_function_block_declaration122)




            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "function_block_declaration"



    # $ANTLR start "fb_io_var_declarations"
    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:102:1: fb_io_var_declarations : ( input_declarations | output_declarations );
    def fb_io_var_declarations(self, ):
        try:
            try:
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:103:2: ( input_declarations | output_declarations )
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == 51) :
                    alt3 = 1
                elif (LA3_0 == 52) :
                    alt3 = 2
                else:
                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae


                if alt3 == 1:
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:103:4: input_declarations
                    pass 
                    self._state.following.append(self.FOLLOW_input_declarations_in_fb_io_var_declarations142)
                    self.input_declarations()

                    self._state.following.pop()


                elif alt3 == 2:
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:104:3: output_declarations
                    pass 
                    self._state.following.append(self.FOLLOW_output_declarations_in_fb_io_var_declarations147)
                    self.output_declarations()

                    self._state.following.pop()



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "fb_io_var_declarations"



    # $ANTLR start "input_declarations"
    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:107:1: input_declarations : 'VAR_INPUT' ( variable_declaration )+ 'END_VAR' ;
    def input_declarations(self, ):
        try:
            try:
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:108:2: ( 'VAR_INPUT' ( variable_declaration )+ 'END_VAR' )
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:108:4: 'VAR_INPUT' ( variable_declaration )+ 'END_VAR'
                pass 
                self.match(self.input, 51, self.FOLLOW_51_in_input_declarations159)

                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:109:3: ( variable_declaration )+
                cnt4 = 0
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == IDENTIFIER) :
                        alt4 = 1


                    if alt4 == 1:
                        # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:109:3: variable_declaration
                        pass 
                        self._state.following.append(self.FOLLOW_variable_declaration_in_input_declarations163)
                        self.variable_declaration()

                        self._state.following.pop()


                    else:
                        if cnt4 >= 1:
                            break #loop4

                        eee = EarlyExitException(4, self.input)
                        raise eee

                    cnt4 += 1


                self.match(self.input, 35, self.FOLLOW_35_in_input_declarations168)




            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "input_declarations"



    # $ANTLR start "output_declarations"
    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:113:1: output_declarations : 'VAR_OUTPUT' ( 'RETAIN' )? ( variable_declaration )+ 'END_VAR' ;
    def output_declarations(self, ):
        try:
            try:
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:114:2: ( 'VAR_OUTPUT' ( 'RETAIN' )? ( variable_declaration )+ 'END_VAR' )
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:114:4: 'VAR_OUTPUT' ( 'RETAIN' )? ( variable_declaration )+ 'END_VAR'
                pass 
                self.match(self.input, 52, self.FOLLOW_52_in_output_declarations180)

                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:114:17: ( 'RETAIN' )?
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if (LA5_0 == 46) :
                    alt5 = 1
                if alt5 == 1:
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:114:17: 'RETAIN'
                    pass 
                    self.match(self.input, 46, self.FOLLOW_46_in_output_declarations182)




                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:115:3: ( variable_declaration )+
                cnt6 = 0
                while True: #loop6
                    alt6 = 2
                    LA6_0 = self.input.LA(1)

                    if (LA6_0 == IDENTIFIER) :
                        alt6 = 1


                    if alt6 == 1:
                        # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:115:3: variable_declaration
                        pass 
                        self._state.following.append(self.FOLLOW_variable_declaration_in_output_declarations187)
                        self.variable_declaration()

                        self._state.following.pop()


                    else:
                        if cnt6 >= 1:
                            break #loop6

                        eee = EarlyExitException(6, self.input)
                        raise eee

                    cnt6 += 1


                self.match(self.input, 35, self.FOLLOW_35_in_output_declarations192)




            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "output_declarations"



    # $ANTLR start "variable_declaration"
    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:119:1: variable_declaration : name= IDENTIFIER ':' type ';' ;
    def variable_declaration(self, ):
        name = None

        try:
            try:
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:120:2: (name= IDENTIFIER ':' type ';' )
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:121:3: name= IDENTIFIER ':' type ';'
                pass 
                name = self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_variable_declaration208)

                self.match(self.input, 23, self.FOLLOW_23_in_variable_declaration210)

                self._state.following.append(self.FOLLOW_type_in_variable_declaration212)
                self.type()

                self._state.following.pop()

                self.match(self.input, 24, self.FOLLOW_24_in_variable_declaration214)

                #action start
                self.scope[name.text] = Variable(name.text)
                #action end





            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "variable_declaration"



    # $ANTLR start "type"
    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:137:1: type : ( 'REAL' | IDENTIFIER );
    def type(self, ):
        try:
            try:
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:137:6: ( 'REAL' | IDENTIFIER )
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:
                pass 
                if self.input.LA(1) in {IDENTIFIER, 45}:
                    self.input.consume()
                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse






            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "type"



    # $ANTLR start "function_block_body"
    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:148:1: function_block_body : ( fuzzify_block )* ( defuzzify_block )* (rb= rule_block )* ;
    def function_block_body(self, ):
        rb = None

        try:
            try:
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:149:2: ( ( fuzzify_block )* ( defuzzify_block )* (rb= rule_block )* )
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:149:4: ( fuzzify_block )* ( defuzzify_block )* (rb= rule_block )*
                pass 
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:149:4: ( fuzzify_block )*
                while True: #loop7
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == 37) :
                        alt7 = 1


                    if alt7 == 1:
                        # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:149:4: fuzzify_block
                        pass 
                        self._state.following.append(self.FOLLOW_fuzzify_block_in_function_block_body250)
                        self.fuzzify_block()

                        self._state.following.pop()


                    else:
                        break #loop7


                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:150:3: ( defuzzify_block )*
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == 30) :
                        alt8 = 1


                    if alt8 == 1:
                        # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:150:3: defuzzify_block
                        pass 
                        self._state.following.append(self.FOLLOW_defuzzify_block_in_function_block_body255)
                        self.defuzzify_block()

                        self._state.following.pop()


                    else:
                        break #loop8


                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:151:3: (rb= rule_block )*
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LA(1)

                    if (LA9_0 == 48) :
                        alt9 = 1


                    if alt9 == 1:
                        # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:151:4: rb= rule_block
                        pass 
                        self._state.following.append(self.FOLLOW_rule_block_in_function_block_body263)
                        rb = self.rule_block()

                        self._state.following.pop()

                        #action start
                        self.system.add_blocks(rb)
                        #action end



                    else:
                        break #loop9





            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "function_block_body"



    # $ANTLR start "rule_block"
    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:155:1: rule_block returns [ruleblock] : 'RULEBLOCK' name= IDENTIFIER operator= operator_definition (activation= activation_method )? accumulation= accumulation_method (r= rule[tnorm, snorm, cnorm] )* 'END_RULEBLOCK' ;
    def rule_block(self, ):
        ruleblock = None


        name = None
        operator = None
        activation = None
        accumulation = None
        r = None

        try:
            try:
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:156:2: ( 'RULEBLOCK' name= IDENTIFIER operator= operator_definition (activation= activation_method )? accumulation= accumulation_method (r= rule[tnorm, snorm, cnorm] )* 'END_RULEBLOCK' )
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:156:4: 'RULEBLOCK' name= IDENTIFIER operator= operator_definition (activation= activation_method )? accumulation= accumulation_method (r= rule[tnorm, snorm, cnorm] )* 'END_RULEBLOCK'
                pass 
                self.match(self.input, 48, self.FOLLOW_48_in_rule_block285)

                name = self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_rule_block289)

                self._state.following.append(self.FOLLOW_operator_definition_in_rule_block295)
                operator = self.operator_definition()

                self._state.following.pop()

                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:158:13: (activation= activation_method )?
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if (LA10_0 == 27) :
                    alt10 = 1
                if alt10 == 1:
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:158:13: activation= activation_method
                    pass 
                    self._state.following.append(self.FOLLOW_activation_method_in_rule_block301)
                    activation = self.activation_method()

                    self._state.following.pop()




                self._state.following.append(self.FOLLOW_accumulation_method_in_rule_block308)
                accumulation = self.accumulation_method()

                self._state.following.pop()

                #action start
                ruleblock = RuleBlock(name.text, operator, activation, accumulation)
                #action end


                #action start
                tnorm = ruleblock.and_
                #action end


                #action start
                snorm = ruleblock.or_
                #action end


                #action start
                cnorm = ruleblock.not_
                #action end


                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:164:3: (r= rule[tnorm, snorm, cnorm] )*
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LA(1)

                    if (LA11_0 == 47) :
                        alt11 = 1


                    if alt11 == 1:
                        # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:164:4: r= rule[tnorm, snorm, cnorm]
                        pass 
                        self._state.following.append(self.FOLLOW_rule_in_rule_block331)
                        r = self.rule(tnorm, snorm, cnorm)

                        self._state.following.pop()

                        #action start
                        ruleblock.addrule(r)
                        #action end



                    else:
                        break #loop11


                self.match(self.input, 34, self.FOLLOW_34_in_rule_block341)




            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return ruleblock

    # $ANTLR end "rule_block"



    # $ANTLR start "operator_definition"
    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:168:1: operator_definition returns [operators] : ( ( ( 'OR' ':' or_= IDENTIFIER ';' ) ( 'AND' ':' and_= IDENTIFIER ';' )? ) | ( ( 'AND' ':' and_= IDENTIFIER ';' ) ( 'OR' ':' or_= IDENTIFIER ';' )? ) ) ( 'NOT' ':' not_= IDENTIFIER ';' )? ;
    def operator_definition(self, ):
        operators = None


        or_ = None
        and_ = None
        not_ = None

        try:
            try:
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:169:2: ( ( ( ( 'OR' ':' or_= IDENTIFIER ';' ) ( 'AND' ':' and_= IDENTIFIER ';' )? ) | ( ( 'AND' ':' and_= IDENTIFIER ';' ) ( 'OR' ':' or_= IDENTIFIER ';' )? ) ) ( 'NOT' ':' not_= IDENTIFIER ';' )? )
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:169:4: ( ( ( 'OR' ':' or_= IDENTIFIER ';' ) ( 'AND' ':' and_= IDENTIFIER ';' )? ) | ( ( 'AND' ':' and_= IDENTIFIER ';' ) ( 'OR' ':' or_= IDENTIFIER ';' )? ) ) ( 'NOT' ':' not_= IDENTIFIER ';' )?
                pass 
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:169:4: ( ( ( 'OR' ':' or_= IDENTIFIER ';' ) ( 'AND' ':' and_= IDENTIFIER ';' )? ) | ( ( 'AND' ':' and_= IDENTIFIER ';' ) ( 'OR' ':' or_= IDENTIFIER ';' )? ) )
                alt14 = 2
                LA14_0 = self.input.LA(1)

                if (LA14_0 == 43) :
                    alt14 = 1
                elif (LA14_0 == 28) :
                    alt14 = 2
                else:
                    nvae = NoViableAltException("", 14, 0, self.input)

                    raise nvae


                if alt14 == 1:
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:169:5: ( ( 'OR' ':' or_= IDENTIFIER ';' ) ( 'AND' ':' and_= IDENTIFIER ';' )? )
                    pass 
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:169:5: ( ( 'OR' ':' or_= IDENTIFIER ';' ) ( 'AND' ':' and_= IDENTIFIER ';' )? )
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:169:6: ( 'OR' ':' or_= IDENTIFIER ';' ) ( 'AND' ':' and_= IDENTIFIER ';' )?
                    pass 
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:169:6: ( 'OR' ':' or_= IDENTIFIER ';' )
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:169:7: 'OR' ':' or_= IDENTIFIER ';'
                    pass 
                    self.match(self.input, 43, self.FOLLOW_43_in_operator_definition358)

                    self.match(self.input, 23, self.FOLLOW_23_in_operator_definition360)

                    or_ = self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_operator_definition364)

                    self.match(self.input, 24, self.FOLLOW_24_in_operator_definition366)




                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:169:36: ( 'AND' ':' and_= IDENTIFIER ';' )?
                    alt12 = 2
                    LA12_0 = self.input.LA(1)

                    if (LA12_0 == 28) :
                        alt12 = 1
                    if alt12 == 1:
                        # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:169:37: 'AND' ':' and_= IDENTIFIER ';'
                        pass 
                        self.match(self.input, 28, self.FOLLOW_28_in_operator_definition370)

                        self.match(self.input, 23, self.FOLLOW_23_in_operator_definition372)

                        and_ = self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_operator_definition376)

                        self.match(self.input, 24, self.FOLLOW_24_in_operator_definition378)








                elif alt14 == 2:
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:170:3: ( ( 'AND' ':' and_= IDENTIFIER ';' ) ( 'OR' ':' or_= IDENTIFIER ';' )? )
                    pass 
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:170:3: ( ( 'AND' ':' and_= IDENTIFIER ';' ) ( 'OR' ':' or_= IDENTIFIER ';' )? )
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:170:4: ( 'AND' ':' and_= IDENTIFIER ';' ) ( 'OR' ':' or_= IDENTIFIER ';' )?
                    pass 
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:170:4: ( 'AND' ':' and_= IDENTIFIER ';' )
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:170:5: 'AND' ':' and_= IDENTIFIER ';'
                    pass 
                    self.match(self.input, 28, self.FOLLOW_28_in_operator_definition389)

                    self.match(self.input, 23, self.FOLLOW_23_in_operator_definition391)

                    and_ = self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_operator_definition395)

                    self.match(self.input, 24, self.FOLLOW_24_in_operator_definition397)




                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:170:36: ( 'OR' ':' or_= IDENTIFIER ';' )?
                    alt13 = 2
                    LA13_0 = self.input.LA(1)

                    if (LA13_0 == 43) :
                        alt13 = 1
                    if alt13 == 1:
                        # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:170:37: 'OR' ':' or_= IDENTIFIER ';'
                        pass 
                        self.match(self.input, 43, self.FOLLOW_43_in_operator_definition401)

                        self.match(self.input, 23, self.FOLLOW_23_in_operator_definition403)

                        or_ = self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_operator_definition407)

                        self.match(self.input, 24, self.FOLLOW_24_in_operator_definition409)










                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:171:3: ( 'NOT' ':' not_= IDENTIFIER ';' )?
                alt15 = 2
                LA15_0 = self.input.LA(1)

                if (LA15_0 == 42) :
                    alt15 = 1
                if alt15 == 1:
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:171:4: 'NOT' ':' not_= IDENTIFIER ';'
                    pass 
                    self.match(self.input, 42, self.FOLLOW_42_in_operator_definition418)

                    self.match(self.input, 23, self.FOLLOW_23_in_operator_definition420)

                    not_ = self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_operator_definition426)

                    self.match(self.input, 24, self.FOLLOW_24_in_operator_definition428)




                #action start
                operators = (and_ and and_.text, or_ and or_.text, not_ and not_.text)
                #action end


                #action start
                operators = check_op(operators)
                #action end





            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return operators

    # $ANTLR end "operator_definition"



    # $ANTLR start "activation_method"
    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:186:1: activation_method returns [activation] : 'ACT' ':' act= IDENTIFIER ';' ;
    def activation_method(self, ):
        activation = None


        act = None

        try:
            try:
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:187:2: ( 'ACT' ':' act= IDENTIFIER ';' )
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:187:4: 'ACT' ':' act= IDENTIFIER ';'
                pass 
                self.match(self.input, 27, self.FOLLOW_27_in_activation_method474)

                self.match(self.input, 23, self.FOLLOW_23_in_activation_method476)

                act = self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_activation_method480)

                self.match(self.input, 24, self.FOLLOW_24_in_activation_method482)

                #action start
                activation = act.text
                #action end





            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return activation

    # $ANTLR end "activation_method"



    # $ANTLR start "accumulation_method"
    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:191:1: accumulation_method returns [accumulation] : 'ACCU' ':' accu= IDENTIFIER ';' ;
    def accumulation_method(self, ):
        accumulation = None


        accu = None

        try:
            try:
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:192:2: ( 'ACCU' ':' accu= IDENTIFIER ';' )
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:192:4: 'ACCU' ':' accu= IDENTIFIER ';'
                pass 
                self.match(self.input, 26, self.FOLLOW_26_in_accumulation_method501)

                self.match(self.input, 23, self.FOLLOW_23_in_accumulation_method503)

                accu = self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_accumulation_method507)

                self.match(self.input, 24, self.FOLLOW_24_in_accumulation_method509)

                #action start
                accumulation = accu.text
                #action end





            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return accumulation

    # $ANTLR end "accumulation_method"



    # $ANTLR start "rule"
    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:196:1: rule[tnorm, snorm, cnorm] returns [rule_] : 'RULE' INTEGRAL_LITERAL ':' 'IF' c1= condition[tnorm, snorm, cnorm] 'THEN' c2= conclusion ( 'WITH' w= weighting_factor )? ';' ;
    def rule(self, tnorm, snorm, cnorm):
        rule_ = None


        c1 = None
        c2 = None
        w = None

        try:
            try:
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:197:2: ( 'RULE' INTEGRAL_LITERAL ':' 'IF' c1= condition[tnorm, snorm, cnorm] 'THEN' c2= conclusion ( 'WITH' w= weighting_factor )? ';' )
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:197:4: 'RULE' INTEGRAL_LITERAL ':' 'IF' c1= condition[tnorm, snorm, cnorm] 'THEN' c2= conclusion ( 'WITH' w= weighting_factor )? ';'
                pass 
                self.match(self.input, 47, self.FOLLOW_47_in_rule529)

                self.match(self.input, INTEGRAL_LITERAL, self.FOLLOW_INTEGRAL_LITERAL_in_rule531)

                self.match(self.input, 23, self.FOLLOW_23_in_rule533)

                self.match(self.input, 38, self.FOLLOW_38_in_rule537)

                self._state.following.append(self.FOLLOW_condition_in_rule541)
                c1 = self.condition(tnorm, snorm, cnorm)

                self._state.following.pop()

                self.match(self.input, 50, self.FOLLOW_50_in_rule544)

                self._state.following.append(self.FOLLOW_conclusion_in_rule548)
                c2 = self.conclusion()

                self._state.following.pop()

                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:198:63: ( 'WITH' w= weighting_factor )?
                alt16 = 2
                LA16_0 = self.input.LA(1)

                if (LA16_0 == 53) :
                    alt16 = 1
                if alt16 == 1:
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:198:64: 'WITH' w= weighting_factor
                    pass 
                    self.match(self.input, 53, self.FOLLOW_53_in_rule551)

                    self._state.following.append(self.FOLLOW_weighting_factor_in_rule555)
                    w = self.weighting_factor()

                    self._state.following.pop()




                self.match(self.input, 24, self.FOLLOW_24_in_rule559)

                #action start
                rule_ = Rule.get_rule(c1, c2, w or 1)
                #action end





            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return rule_

    # $ANTLR end "rule"



    # $ANTLR start "condition"
    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:202:1: condition[tnorm, snorm, cnorm] returns [operator_tree] : res= expr[tnorm, snorm, cnorm] ;
    def condition(self, tnorm, snorm, cnorm):
        operator_tree = None


        res = None

        try:
            try:
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:203:2: (res= expr[tnorm, snorm, cnorm] )
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:203:4: res= expr[tnorm, snorm, cnorm]
                pass 
                self._state.following.append(self.FOLLOW_expr_in_condition580)
                res = self.expr(tnorm, snorm, cnorm)

                self._state.following.pop()

                #action start
                operator_tree = res
                #action end





            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return operator_tree

    # $ANTLR end "condition"



    # $ANTLR start "expr"
    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:206:1: expr[tnorm, snorm, cnorm] returns [res] : t= term[tnorm, snorm, cnorm] ( 'OR' e= expr[tnorm, snorm, cnorm] )? ;
    def expr(self, tnorm, snorm, cnorm):
        res = None


        t = None
        e = None

        try:
            try:
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:207:2: (t= term[tnorm, snorm, cnorm] ( 'OR' e= expr[tnorm, snorm, cnorm] )? )
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:207:4: t= term[tnorm, snorm, cnorm] ( 'OR' e= expr[tnorm, snorm, cnorm] )?
                pass 
                self._state.following.append(self.FOLLOW_term_in_expr602)
                t = self.term(tnorm, snorm, cnorm)

                self._state.following.pop()

                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:208:3: ( 'OR' e= expr[tnorm, snorm, cnorm] )?
                alt17 = 2
                LA17_0 = self.input.LA(1)

                if (LA17_0 == 43) :
                    alt17 = 1
                if alt17 == 1:
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:208:4: 'OR' e= expr[tnorm, snorm, cnorm]
                    pass 
                    self.match(self.input, 43, self.FOLLOW_43_in_expr608)

                    self._state.following.append(self.FOLLOW_expr_in_expr614)
                    e = self.expr(tnorm, snorm, cnorm)

                    self._state.following.pop()




                #action start
                res = Or(t, e, snorm) if e is not None else t
                #action end





            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return res

    # $ANTLR end "expr"



    # $ANTLR start "term"
    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:219:1: term[tnorm, snorm, cnorm] returns [t] : (e= pred[cnorm] | (n= 'NOT' )? '(' e= expr[tnorm, snorm, cnorm] ')' ) ( 'AND' t_= term[tnorm, snorm, cnorm] )? ;
    def term(self, tnorm, snorm, cnorm):
        t = None


        n = None
        e = None
        t_ = None

        try:
            try:
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:220:2: ( (e= pred[cnorm] | (n= 'NOT' )? '(' e= expr[tnorm, snorm, cnorm] ')' ) ( 'AND' t_= term[tnorm, snorm, cnorm] )? )
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:220:4: (e= pred[cnorm] | (n= 'NOT' )? '(' e= expr[tnorm, snorm, cnorm] ')' ) ( 'AND' t_= term[tnorm, snorm, cnorm] )?
                pass 
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:220:4: (e= pred[cnorm] | (n= 'NOT' )? '(' e= expr[tnorm, snorm, cnorm] ')' )
                alt19 = 2
                LA19_0 = self.input.LA(1)

                if (LA19_0 == IDENTIFIER) :
                    alt19 = 1
                elif (LA19_0 in {14, 42}) :
                    alt19 = 2
                else:
                    nvae = NoViableAltException("", 19, 0, self.input)

                    raise nvae


                if alt19 == 1:
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:220:6: e= pred[cnorm]
                    pass 
                    self._state.following.append(self.FOLLOW_pred_in_term643)
                    e = self.pred(cnorm)

                    self._state.following.pop()


                elif alt19 == 2:
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:220:22: (n= 'NOT' )? '(' e= expr[tnorm, snorm, cnorm] ')'
                    pass 
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:220:23: (n= 'NOT' )?
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 == 42) :
                        alt18 = 1
                    if alt18 == 1:
                        # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:220:23: n= 'NOT'
                        pass 
                        n = self.match(self.input, 42, self.FOLLOW_42_in_term650)




                    self.match(self.input, 14, self.FOLLOW_14_in_term653)

                    self._state.following.append(self.FOLLOW_expr_in_term657)
                    e = self.expr(tnorm, snorm, cnorm)

                    self._state.following.pop()

                    self.match(self.input, 15, self.FOLLOW_15_in_term660)




                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:221:3: ( 'AND' t_= term[tnorm, snorm, cnorm] )?
                alt20 = 2
                LA20_0 = self.input.LA(1)

                if (LA20_0 == 28) :
                    alt20 = 1
                if alt20 == 1:
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:221:4: 'AND' t_= term[tnorm, snorm, cnorm]
                    pass 
                    self.match(self.input, 28, self.FOLLOW_28_in_term667)

                    self._state.following.append(self.FOLLOW_term_in_term672)
                    t_ = self.term(tnorm, snorm, cnorm)

                    self._state.following.pop()




                #action start
                t = e if n is None else Not(e, cnorm)
                #action end


                #action start
                t = t if t_ is None else And(t,t_, tnorm)
                #action end





            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return t

    # $ANTLR end "term"



    # $ANTLR start "pred"
    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:230:1: pred[cnorm] returns [res] : var= IDENTIFIER 'IS' (n= 'NOT' )? t= IDENTIFIER ;
    def pred(self, cnorm):
        res = None


        var = None
        n = None
        t = None

        try:
            try:
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:231:2: (var= IDENTIFIER 'IS' (n= 'NOT' )? t= IDENTIFIER )
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:231:4: var= IDENTIFIER 'IS' (n= 'NOT' )? t= IDENTIFIER
                pass 
                var = self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_pred703)

                self.match(self.input, 39, self.FOLLOW_39_in_pred705)

                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:231:24: (n= 'NOT' )?
                alt21 = 2
                LA21_0 = self.input.LA(1)

                if (LA21_0 == 42) :
                    alt21 = 1
                if alt21 == 1:
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:231:25: n= 'NOT'
                    pass 
                    n = self.match(self.input, 42, self.FOLLOW_42_in_pred710)




                t = self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_pred716)

                #action start
                p = Predicate(self.scope[var.text], self.scope[var.text + t.text])
                #action end


                #action start
                res = p if n is None else Not(p, cnorm)
                #action end





            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return res

    # $ANTLR end "pred"



    # $ANTLR start "conclusion"
    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:254:1: conclusion returns [res] : c= ( mconclusion | sconclusion ) ;
    def conclusion(self, ):
        res = None


        c = None

        try:
            try:
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:255:2: (c= ( mconclusion | sconclusion ) )
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:257:3: c= ( mconclusion | sconclusion )
                pass 
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:257:7: ( mconclusion | sconclusion )
                alt22 = 2
                LA22_0 = self.input.LA(1)

                if (LA22_0 == IDENTIFIER) :
                    LA22_1 = self.input.LA(2)

                    if (LA22_1 in {20, 39}) :
                        alt22 = 1
                    elif (LA22_1 in {16, 17, 19, 22, 24, 53}) :
                        alt22 = 2
                    else:
                        nvae = NoViableAltException("", 22, 1, self.input)

                        raise nvae


                elif (LA22_0 in {INTEGRAL_LITERAL, REAL_LITERAL}) :
                    alt22 = 2
                else:
                    nvae = NoViableAltException("", 22, 0, self.input)

                    raise nvae


                if alt22 == 1:
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:257:8: mconclusion
                    pass 
                    self._state.following.append(self.FOLLOW_mconclusion_in_conclusion756)
                    c = self.mconclusion()

                    self._state.following.pop()


                elif alt22 == 2:
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:257:22: sconclusion
                    pass 
                    self._state.following.append(self.FOLLOW_sconclusion_in_conclusion760)
                    c = self.sconclusion()

                    self._state.following.pop()




                #action start
                res = c
                #action end





            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return res

    # $ANTLR end "conclusion"



    # $ANTLR start "mconclusion"
    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:261:1: mconclusion returns [res] : var= IDENTIFIER ( 'IS' | '.' ) t= IDENTIFIER ( ',' var_= IDENTIFIER ( 'IS' | '.' ) t_= IDENTIFIER )* ;
    def mconclusion(self, ):
        res = None


        var = None
        t = None
        var_ = None
        t_ = None


        res = []

        try:
            try:
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:269:2: (var= IDENTIFIER ( 'IS' | '.' ) t= IDENTIFIER ( ',' var_= IDENTIFIER ( 'IS' | '.' ) t_= IDENTIFIER )* )
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:269:4: var= IDENTIFIER ( 'IS' | '.' ) t= IDENTIFIER ( ',' var_= IDENTIFIER ( 'IS' | '.' ) t_= IDENTIFIER )*
                pass 
                var = self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_mconclusion789)

                if self.input.LA(1) in {20, 39}:
                    self.input.consume()
                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse



                t = self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_mconclusion801)

                #action start
                res.append(Predicate(self.scope[var.text], self.scope[var.text + t.text]))
                #action end


                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:270:3: ( ',' var_= IDENTIFIER ( 'IS' | '.' ) t_= IDENTIFIER )*
                while True: #loop23
                    alt23 = 2
                    LA23_0 = self.input.LA(1)

                    if (LA23_0 == 18) :
                        alt23 = 1


                    if alt23 == 1:
                        # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:270:4: ',' var_= IDENTIFIER ( 'IS' | '.' ) t_= IDENTIFIER
                        pass 
                        self.match(self.input, 18, self.FOLLOW_18_in_mconclusion808)

                        var_ = self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_mconclusion812)

                        if self.input.LA(1) in {20, 39}:
                            self.input.consume()
                            self._state.errorRecovery = False


                        else:
                            mse = MismatchedSetException(None, self.input)
                            raise mse



                        t_ = self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_mconclusion824)

                        #action start
                        res.append(Predicate(self.scope[var_.text], self.scope[var_.text + t_.text]))
                        #action end



                    else:
                        break #loop23




                #action start

                if self.type_ == '_TSUKAMOTO_':
                	res = res[0]

                #action end


            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return res

    # $ANTLR end "mconclusion"



    # $ANTLR start "sconclusion"
    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:273:1: sconclusion returns [res] : (i= IDENTIFIER |n= numeric_literal ) (o= ( '+' | '-' | '*' ( '*' )? | '/' ( '/' )? ) sc= sconclusion )? ;
    def sconclusion(self, ):
        res = None


        i = None
        o = None
        n = None
        sc = None

        try:
            try:
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:274:2: ( (i= IDENTIFIER |n= numeric_literal ) (o= ( '+' | '-' | '*' ( '*' )? | '/' ( '/' )? ) sc= sconclusion )? )
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:274:4: (i= IDENTIFIER |n= numeric_literal ) (o= ( '+' | '-' | '*' ( '*' )? | '/' ( '/' )? ) sc= sconclusion )?
                pass 
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:274:4: (i= IDENTIFIER |n= numeric_literal )
                alt24 = 2
                LA24_0 = self.input.LA(1)

                if (LA24_0 == IDENTIFIER) :
                    alt24 = 1
                elif (LA24_0 in {INTEGRAL_LITERAL, REAL_LITERAL}) :
                    alt24 = 2
                else:
                    nvae = NoViableAltException("", 24, 0, self.input)

                    raise nvae


                if alt24 == 1:
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:274:5: i= IDENTIFIER
                    pass 
                    i = self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_sconclusion847)


                elif alt24 == 2:
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:274:20: n= numeric_literal
                    pass 
                    self._state.following.append(self.FOLLOW_numeric_literal_in_sconclusion853)
                    n = self.numeric_literal()

                    self._state.following.pop()




                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:274:39: (o= ( '+' | '-' | '*' ( '*' )? | '/' ( '/' )? ) sc= sconclusion )?
                alt28 = 2
                LA28_0 = self.input.LA(1)

                if (LA28_0 in {16, 17, 19, 22}) :
                    alt28 = 1
                if alt28 == 1:
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:274:40: o= ( '+' | '-' | '*' ( '*' )? | '/' ( '/' )? ) sc= sconclusion
                    pass 
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:274:42: ( '+' | '-' | '*' ( '*' )? | '/' ( '/' )? )
                    alt27 = 4
                    LA27 = self.input.LA(1)
                    if LA27 in {17}:
                        alt27 = 1
                    elif LA27 in {19}:
                        alt27 = 2
                    elif LA27 in {16}:
                        alt27 = 3
                    elif LA27 in {22}:
                        alt27 = 4
                    else:
                        nvae = NoViableAltException("", 27, 0, self.input)

                        raise nvae


                    if alt27 == 1:
                        # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:274:43: '+'
                        pass 
                        o = self.match(self.input, 17, self.FOLLOW_17_in_sconclusion860)


                    elif alt27 == 2:
                        # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:274:47: '-'
                        pass 
                        o = self.match(self.input, 19, self.FOLLOW_19_in_sconclusion862)


                    elif alt27 == 3:
                        # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:274:51: '*' ( '*' )?
                        pass 
                        o = self.match(self.input, 16, self.FOLLOW_16_in_sconclusion864)

                        # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:274:54: ( '*' )?
                        alt25 = 2
                        LA25_0 = self.input.LA(1)

                        if (LA25_0 == 16) :
                            alt25 = 1
                        if alt25 == 1:
                            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:274:54: '*'
                            pass 
                            o = self.match(self.input, 16, self.FOLLOW_16_in_sconclusion865)





                    elif alt27 == 4:
                        # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:274:59: '/' ( '/' )?
                        pass 
                        o = self.match(self.input, 22, self.FOLLOW_22_in_sconclusion868)

                        # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:274:62: ( '/' )?
                        alt26 = 2
                        LA26_0 = self.input.LA(1)

                        if (LA26_0 == 22) :
                            alt26 = 1
                        if alt26 == 1:
                            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:274:62: '/'
                            pass 
                            o = self.match(self.input, 22, self.FOLLOW_22_in_sconclusion869)







                    self._state.following.append(self.FOLLOW_sconclusion_in_sconclusion875)
                    sc = self.sconclusion()

                    self._state.following.pop()




                #action start
                s = i.text if i is not None else ((n is not None) and [self.input.toString(n.start,n.stop)] or [None])[0]
                #action end


                #action start
                res = s + o.text + sc if sc is not None else s
                #action end





            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return res

    # $ANTLR end "sconclusion"



    # $ANTLR start "tconclusion"
    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:279:1: tconclusion returns [res] : var= IDENTIFIER ( 'IS' | '.' ) t= IDENTIFIER ;
    def tconclusion(self, ):
        res = None


        var = None
        t = None


        res = None

        try:
            try:
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:283:2: (var= IDENTIFIER ( 'IS' | '.' ) t= IDENTIFIER )
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:283:4: var= IDENTIFIER ( 'IS' | '.' ) t= IDENTIFIER
                pass 
                var = self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_tconclusion906)

                if self.input.LA(1) in {20, 39}:
                    self.input.consume()
                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse



                t = self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_tconclusion918)

                #action start
                res = Predicate(self.scope[var.text], self.scope[var.text + t.text])
                #action end





            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return res

    # $ANTLR end "tconclusion"



    # $ANTLR start "weighting_factor"
    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:286:1: weighting_factor returns [value] : (name= IDENTIFIER |n= numeric_literal );
    def weighting_factor(self, ):
        value = None


        name = None
        n = None

        try:
            try:
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:287:2: (name= IDENTIFIER |n= numeric_literal )
                alt29 = 2
                LA29_0 = self.input.LA(1)

                if (LA29_0 == IDENTIFIER) :
                    alt29 = 1
                elif (LA29_0 in {INTEGRAL_LITERAL, REAL_LITERAL}) :
                    alt29 = 2
                else:
                    nvae = NoViableAltException("", 29, 0, self.input)

                    raise nvae


                if alt29 == 1:
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:287:4: name= IDENTIFIER
                    pass 
                    name = self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_weighting_factor936)

                    #action start
                    value = scope[name.text]
                    #action end



                elif alt29 == 2:
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:288:3: n= numeric_literal
                    pass 
                    self._state.following.append(self.FOLLOW_numeric_literal_in_weighting_factor946)
                    n = self.numeric_literal()

                    self._state.following.pop()

                    #action start
                    value = float(((n is not None) and [self.input.toString(n.start,n.stop)] or [None])[0])
                    #action end




            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "weighting_factor"



    # $ANTLR start "fuzzify_block"
    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:291:1: fuzzify_block : 'FUZZIFY' name= IDENTIFIER (adjective= linguistic_term[variable] )* 'END_FUZZIFY' ;
    def fuzzify_block(self, ):
        name = None
        adjective = None

        try:
            try:
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:292:2: ( 'FUZZIFY' name= IDENTIFIER (adjective= linguistic_term[variable] )* 'END_FUZZIFY' )
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:292:4: 'FUZZIFY' name= IDENTIFIER (adjective= linguistic_term[variable] )* 'END_FUZZIFY'
                pass 
                self.match(self.input, 37, self.FOLLOW_37_in_fuzzify_block959)

                name = self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_fuzzify_block963)

                #action start
                variable = self.scope[name.text]
                #action end


                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:294:3: (adjective= linguistic_term[variable] )*
                while True: #loop30
                    alt30 = 2
                    LA30_0 = self.input.LA(1)

                    if (LA30_0 == 49) :
                        alt30 = 1


                    if alt30 == 1:
                        # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:294:4: adjective= linguistic_term[variable]
                        pass 
                        self._state.following.append(self.FOLLOW_linguistic_term_in_fuzzify_block974)
                        adjective = self.linguistic_term(variable)

                        self._state.following.pop()


                    else:
                        break #loop30


                self.match(self.input, 33, self.FOLLOW_33_in_fuzzify_block982)




            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "fuzzify_block"



    # $ANTLR start "defuzzify_block"
    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:298:1: defuzzify_block : 'DEFUZZIFY' name= IDENTIFIER (adjective= linguistic_term[variable] )* defuzzification= defuzzification_method default= default_value (r= range )? 'END_DEFUZZIFY' ;
    def defuzzify_block(self, ):
        name = None
        adjective = None
        defuzzification = None
        default = None
        r = None

        try:
            try:
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:299:2: ( 'DEFUZZIFY' name= IDENTIFIER (adjective= linguistic_term[variable] )* defuzzification= defuzzification_method default= default_value (r= range )? 'END_DEFUZZIFY' )
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:299:4: 'DEFUZZIFY' name= IDENTIFIER (adjective= linguistic_term[variable] )* defuzzification= defuzzification_method default= default_value (r= range )? 'END_DEFUZZIFY'
                pass 
                self.match(self.input, 30, self.FOLLOW_30_in_defuzzify_block993)

                name = self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_defuzzify_block997)

                #action start
                variable = self.scope[name.text]
                #action end


                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:300:3: (adjective= linguistic_term[variable] )*
                while True: #loop31
                    alt31 = 2
                    LA31_0 = self.input.LA(1)

                    if (LA31_0 == 49) :
                        alt31 = 1


                    if alt31 == 1:
                        # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:300:4: adjective= linguistic_term[variable]
                        pass 
                        self._state.following.append(self.FOLLOW_linguistic_term_in_defuzzify_block1006)
                        adjective = self.linguistic_term(variable)

                        self._state.following.pop()


                    else:
                        break #loop31


                self._state.following.append(self.FOLLOW_defuzzification_method_in_defuzzify_block1016)
                defuzzification = self.defuzzification_method()

                self._state.following.pop()

                #action start
                variable.defuzzification = defuzzification
                #action end


                self._state.following.append(self.FOLLOW_default_value_in_defuzzify_block1026)
                default = self.default_value()

                self._state.following.pop()

                #action start
                variable.default = default
                #action end


                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:305:4: (r= range )?
                alt32 = 2
                LA32_0 = self.input.LA(1)

                if (LA32_0 == 44) :
                    alt32 = 1
                if alt32 == 1:
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:305:4: r= range
                    pass 
                    self._state.following.append(self.FOLLOW_range_in_defuzzify_block1036)
                    r = self.range()

                    self._state.following.pop()




                self.match(self.input, 31, self.FOLLOW_31_in_defuzzify_block1041)




            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "defuzzify_block"


    class variable_name_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()






    # $ANTLR start "variable_name"
    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:309:1: variable_name : IDENTIFIER ;
    def variable_name(self, ):
        retval = self.variable_name_return()
        retval.start = self.input.LT(1)


        try:
            try:
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:309:15: ( IDENTIFIER )
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:309:17: IDENTIFIER
                pass 
                self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_variable_name1051)



                retval.stop = self.input.LT(-1)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "variable_name"



    # $ANTLR start "linguistic_term"
    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:311:1: linguistic_term[variable] returns [adjective] : 'TERM' name= IDENTIFIER ':' '=' fset= membership_function ';' ;
    def linguistic_term(self, variable):
        adjective = None


        name = None
        fset = None

        try:
            try:
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:312:2: ( 'TERM' name= IDENTIFIER ':' '=' fset= membership_function ';' )
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:312:4: 'TERM' name= IDENTIFIER ':' '=' fset= membership_function ';'
                pass 
                self.match(self.input, 49, self.FOLLOW_49_in_linguistic_term1065)

                name = self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_linguistic_term1069)

                self.match(self.input, 23, self.FOLLOW_23_in_linguistic_term1071)

                self.match(self.input, 25, self.FOLLOW_25_in_linguistic_term1072)

                self._state.following.append(self.FOLLOW_membership_function_in_linguistic_term1076)
                fset = self.membership_function()

                self._state.following.pop()

                self.match(self.input, 24, self.FOLLOW_24_in_linguistic_term1078)

                #action start
                adjective = Adjective(name.text, fset)
                #action end


                #action start
                variable.adjectives.append(adjective)
                #action end


                #action start
                self.scope[variable.name + name.text]=adjective
                #action end





            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return adjective

    # $ANTLR end "linguistic_term"



    # $ANTLR start "term_name"
    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:318:1: term_name : IDENTIFIER ;
    def term_name(self, ):
        try:
            try:
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:318:11: ( IDENTIFIER )
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:318:13: IDENTIFIER
                pass 
                self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_term_name1100)




            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return 

    # $ANTLR end "term_name"



    # $ANTLR start "membership_function"
    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:320:1: membership_function returns [fuzzy_set] : fset= ( singleton | points | other_function ) ;
    def membership_function(self, ):
        fuzzy_set = None


        fset = None

        try:
            try:
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:321:2: (fset= ( singleton | points | other_function ) )
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:321:4: fset= ( singleton | points | other_function )
                pass 
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:321:11: ( singleton | points | other_function )
                alt33 = 3
                LA33 = self.input.LA(1)
                if LA33 in {INTEGRAL_LITERAL, REAL_LITERAL}:
                    alt33 = 1
                elif LA33 in {IDENTIFIER}:
                    LA33_2 = self.input.LA(2)

                    if (LA33_2 == 14) :
                        alt33 = 3
                    elif (LA33_2 == 24) :
                        alt33 = 1
                    else:
                        nvae = NoViableAltException("", 33, 2, self.input)

                        raise nvae


                elif LA33 in {14, 24}:
                    alt33 = 2
                else:
                    nvae = NoViableAltException("", 33, 0, self.input)

                    raise nvae


                if alt33 == 1:
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:321:13: singleton
                    pass 
                    self._state.following.append(self.FOLLOW_singleton_in_membership_function1119)
                    fset = self.singleton()

                    self._state.following.pop()


                elif alt33 == 2:
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:321:25: points
                    pass 
                    self._state.following.append(self.FOLLOW_points_in_membership_function1123)
                    fset = self.points()

                    self._state.following.pop()


                elif alt33 == 3:
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:321:34: other_function
                    pass 
                    self._state.following.append(self.FOLLOW_other_function_in_membership_function1127)
                    fset = self.other_function()

                    self._state.following.pop()




                #action start
                fuzzy_set = fset
                #action end





            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return fuzzy_set

    # $ANTLR end "membership_function"



    # $ANTLR start "singleton"
    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:325:1: singleton returns [fset] : ( (n= numeric_literal ) | (v= variable_name ) );
    def singleton(self, ):
        fset = None


        n = None
        v = None

        try:
            try:
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:326:2: ( (n= numeric_literal ) | (v= variable_name ) )
                alt34 = 2
                LA34_0 = self.input.LA(1)

                if (LA34_0 in {INTEGRAL_LITERAL, REAL_LITERAL}) :
                    alt34 = 1
                elif (LA34_0 == IDENTIFIER) :
                    alt34 = 2
                else:
                    nvae = NoViableAltException("", 34, 0, self.input)

                    raise nvae


                if alt34 == 1:
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:326:4: (n= numeric_literal )
                    pass 
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:326:4: (n= numeric_literal )
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:326:5: n= numeric_literal
                    pass 
                    self._state.following.append(self.FOLLOW_numeric_literal_in_singleton1149)
                    n = self.numeric_literal()

                    self._state.following.pop()

                    #action start
                    fset = get_fset('Singleton', [float(((n is not None) and [self.input.toString(n.start,n.stop)] or [None])[0])])
                    #action end






                elif alt34 == 2:
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:328:3: (v= variable_name )
                    pass 
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:328:3: (v= variable_name )
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:328:4: v= variable_name
                    pass 
                    self._state.following.append(self.FOLLOW_variable_name_in_singleton1164)
                    v = self.variable_name()

                    self._state.following.pop()

                    #action start
                    fset = get_fset('Singleton', self.scope[((v is not None) and [self.input.toString(v.start,v.stop)] or [None])[0]]) 
                    #action end







            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return fset

    # $ANTLR end "singleton"



    # $ANTLR start "points"
    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:331:1: points returns [fset] : ( '(' (x= numeric_literal | variable_name ) ',' y= numeric_literal ')' )* ;
    def points(self, ):
        fset = None


        x = None
        y = None


        points=[]

        try:
            try:
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:335:2: ( ( '(' (x= numeric_literal | variable_name ) ',' y= numeric_literal ')' )* )
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:335:4: ( '(' (x= numeric_literal | variable_name ) ',' y= numeric_literal ')' )*
                pass 
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:335:4: ( '(' (x= numeric_literal | variable_name ) ',' y= numeric_literal ')' )*
                while True: #loop36
                    alt36 = 2
                    LA36_0 = self.input.LA(1)

                    if (LA36_0 == 14) :
                        alt36 = 1


                    if alt36 == 1:
                        # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:335:5: '(' (x= numeric_literal | variable_name ) ',' y= numeric_literal ')'
                        pass 
                        self.match(self.input, 14, self.FOLLOW_14_in_points1187)

                        # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:335:9: (x= numeric_literal | variable_name )
                        alt35 = 2
                        LA35_0 = self.input.LA(1)

                        if (LA35_0 in {INTEGRAL_LITERAL, REAL_LITERAL}) :
                            alt35 = 1
                        elif (LA35_0 == IDENTIFIER) :
                            alt35 = 2
                        else:
                            nvae = NoViableAltException("", 35, 0, self.input)

                            raise nvae


                        if alt35 == 1:
                            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:335:10: x= numeric_literal
                            pass 
                            self._state.following.append(self.FOLLOW_numeric_literal_in_points1192)
                            x = self.numeric_literal()

                            self._state.following.pop()


                        elif alt35 == 2:
                            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:335:28: variable_name
                            pass 
                            self._state.following.append(self.FOLLOW_variable_name_in_points1194)
                            self.variable_name()

                            self._state.following.pop()




                        self.match(self.input, 18, self.FOLLOW_18_in_points1197)

                        self._state.following.append(self.FOLLOW_numeric_literal_in_points1201)
                        y = self.numeric_literal()

                        self._state.following.pop()

                        self.match(self.input, 15, self.FOLLOW_15_in_points1203)

                        #action start
                        points.append((float(((x is not None) and [self.input.toString(x.start,x.stop)] or [None])[0]), float(((y is not None) and [self.input.toString(y.start,y.stop)] or [None])[0])))
                        #action end



                    else:
                        break #loop36


                #action start
                fset = get_fset('Polygon', points)
                #action end





            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return fset

    # $ANTLR end "points"



    # $ANTLR start "defuzzification_method"
    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:341:1: defuzzification_method returns [method] : 'METHOD' ':' m= IDENTIFIER ';' ;
    def defuzzification_method(self, ):
        method = None


        m = None

        try:
            try:
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:342:2: ( 'METHOD' ':' m= IDENTIFIER ';' )
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:342:4: 'METHOD' ':' m= IDENTIFIER ';'
                pass 
                self.match(self.input, 40, self.FOLLOW_40_in_defuzzification_method1231)

                self.match(self.input, 23, self.FOLLOW_23_in_defuzzification_method1233)

                m = self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_defuzzification_method1237)

                self.match(self.input, 24, self.FOLLOW_24_in_defuzzification_method1239)

                #action start
                method = m.text
                #action end





            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return method

    # $ANTLR end "defuzzification_method"



    # $ANTLR start "other_function"
    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:345:1: other_function returns [fset] : name= IDENTIFIER '(' (p= function_param ( ',' p_= function_param )* )? ')' ;
    def other_function(self, ):
        fset = None


        name = None
        p = None
        p_ = None


        params = []

        try:
            try:
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:349:2: (name= IDENTIFIER '(' (p= function_param ( ',' p_= function_param )* )? ')' )
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:349:4: name= IDENTIFIER '(' (p= function_param ( ',' p_= function_param )* )? ')'
                pass 
                name = self.match(self.input, IDENTIFIER, self.FOLLOW_IDENTIFIER_in_other_function1263)

                self.match(self.input, 14, self.FOLLOW_14_in_other_function1267)

                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:351:3: (p= function_param ( ',' p_= function_param )* )?
                alt38 = 2
                LA38_0 = self.input.LA(1)

                if (LA38_0 in {INTEGRAL_LITERAL, REAL_LITERAL, 14}) :
                    alt38 = 1
                if alt38 == 1:
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:351:4: p= function_param ( ',' p_= function_param )*
                    pass 
                    self._state.following.append(self.FOLLOW_function_param_in_other_function1276)
                    p = self.function_param()

                    self._state.following.pop()

                    #action start
                    params.append(p)
                    #action end


                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:352:3: ( ',' p_= function_param )*
                    while True: #loop37
                        alt37 = 2
                        LA37_0 = self.input.LA(1)

                        if (LA37_0 == 18) :
                            alt37 = 1


                        if alt37 == 1:
                            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:352:4: ',' p_= function_param
                            pass 
                            self.match(self.input, 18, self.FOLLOW_18_in_other_function1283)

                            self._state.following.append(self.FOLLOW_function_param_in_other_function1287)
                            p_ = self.function_param()

                            self._state.following.pop()

                            #action start
                            params.append(p_)
                            #action end



                        else:
                            break #loop37





                self.match(self.input, 15, self.FOLLOW_15_in_other_function1300)

                #action start
                fset = get_fset(name.text, params)
                #action end





            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return fset

    # $ANTLR end "other_function"



    # $ANTLR start "function_param"
    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:358:1: function_param returns [param] : (p= numeric_literal | ( '(' x= numeric_literal ',' y= numeric_literal ')' ) );
    def function_param(self, ):
        param = None


        p = None
        x = None
        y = None

        try:
            try:
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:359:2: (p= numeric_literal | ( '(' x= numeric_literal ',' y= numeric_literal ')' ) )
                alt39 = 2
                LA39_0 = self.input.LA(1)

                if (LA39_0 in {INTEGRAL_LITERAL, REAL_LITERAL}) :
                    alt39 = 1
                elif (LA39_0 == 14) :
                    alt39 = 2
                else:
                    nvae = NoViableAltException("", 39, 0, self.input)

                    raise nvae


                if alt39 == 1:
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:359:5: p= numeric_literal
                    pass 
                    self._state.following.append(self.FOLLOW_numeric_literal_in_function_param1321)
                    p = self.numeric_literal()

                    self._state.following.pop()

                    #action start
                    param = float(((p is not None) and [self.input.toString(p.start,p.stop)] or [None])[0])
                    #action end



                elif alt39 == 2:
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:360:3: ( '(' x= numeric_literal ',' y= numeric_literal ')' )
                    pass 
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:360:3: ( '(' x= numeric_literal ',' y= numeric_literal ')' )
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:360:5: '(' x= numeric_literal ',' y= numeric_literal ')'
                    pass 
                    self.match(self.input, 14, self.FOLLOW_14_in_function_param1331)

                    self._state.following.append(self.FOLLOW_numeric_literal_in_function_param1335)
                    x = self.numeric_literal()

                    self._state.following.pop()

                    self.match(self.input, 18, self.FOLLOW_18_in_function_param1337)

                    self._state.following.append(self.FOLLOW_numeric_literal_in_function_param1341)
                    y = self.numeric_literal()

                    self._state.following.pop()

                    self.match(self.input, 15, self.FOLLOW_15_in_function_param1343)

                    #action start
                    param = (float(((x is not None) and [self.input.toString(x.start,x.stop)] or [None])[0]), float(((y is not None) and [self.input.toString(y.start,y.stop)] or [None])[0]))
                    #action end







            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return param

    # $ANTLR end "function_param"



    # $ANTLR start "default_value"
    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:365:1: default_value returns [value] : 'DEFAULT' ':' '=' (num= numeric_literal | 'NC' ) ';' ;
    def default_value(self, ):
        value = None


        num = None


        value = None

        try:
            try:
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:369:2: ( 'DEFAULT' ':' '=' (num= numeric_literal | 'NC' ) ';' )
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:369:4: 'DEFAULT' ':' '=' (num= numeric_literal | 'NC' ) ';'
                pass 
                self.match(self.input, 29, self.FOLLOW_29_in_default_value1367)

                self.match(self.input, 23, self.FOLLOW_23_in_default_value1369)

                self.match(self.input, 25, self.FOLLOW_25_in_default_value1370)

                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:370:3: (num= numeric_literal | 'NC' )
                alt40 = 2
                LA40_0 = self.input.LA(1)

                if (LA40_0 in {INTEGRAL_LITERAL, REAL_LITERAL}) :
                    alt40 = 1
                elif (LA40_0 == 41) :
                    alt40 = 2
                else:
                    nvae = NoViableAltException("", 40, 0, self.input)

                    raise nvae


                if alt40 == 1:
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:370:4: num= numeric_literal
                    pass 
                    self._state.following.append(self.FOLLOW_numeric_literal_in_default_value1377)
                    num = self.numeric_literal()

                    self._state.following.pop()

                    #action start
                    value=float(((num is not None) and [self.input.toString(num.start,num.stop)] or [None])[0])
                    #action end



                elif alt40 == 2:
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:372:3: 'NC'
                    pass 
                    self.match(self.input, 41, self.FOLLOW_41_in_default_value1387)




                self.match(self.input, 24, self.FOLLOW_24_in_default_value1392)




            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return value

    # $ANTLR end "default_value"



    # $ANTLR start "range"
    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:376:1: range returns [interval] : 'RANGE' ':' '=' '(' x= numeric_literal '..' y= numeric_literal ')' ';' ;
    def range(self, ):
        interval = None


        x = None
        y = None

        try:
            try:
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:377:2: ( 'RANGE' ':' '=' '(' x= numeric_literal '..' y= numeric_literal ')' ';' )
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:377:4: 'RANGE' ':' '=' '(' x= numeric_literal '..' y= numeric_literal ')' ';'
                pass 
                self.match(self.input, 44, self.FOLLOW_44_in_range1406)

                self.match(self.input, 23, self.FOLLOW_23_in_range1408)

                self.match(self.input, 25, self.FOLLOW_25_in_range1409)

                self.match(self.input, 14, self.FOLLOW_14_in_range1411)

                self._state.following.append(self.FOLLOW_numeric_literal_in_range1415)
                x = self.numeric_literal()

                self._state.following.pop()

                self.match(self.input, 21, self.FOLLOW_21_in_range1417)

                self._state.following.append(self.FOLLOW_numeric_literal_in_range1421)
                y = self.numeric_literal()

                self._state.following.pop()

                self.match(self.input, 15, self.FOLLOW_15_in_range1423)

                self.match(self.input, 24, self.FOLLOW_24_in_range1425)

                #action start
                interval = Interval(float(((x is not None) and [self.input.toString(x.start,x.stop)] or [None])[0]), float(((y is not None) and [self.input.toString(y.start,y.stop)] or [None])[0]))
                #action end





            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return interval

    # $ANTLR end "range"


    class numeric_literal_return(ParserRuleReturnScope):
        def __init__(self):
            super().__init__()






    # $ANTLR start "numeric_literal"
    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:386:1: numeric_literal : ( INTEGRAL_LITERAL | REAL_LITERAL );
    def numeric_literal(self, ):
        retval = self.numeric_literal_return()
        retval.start = self.input.LT(1)


        try:
            try:
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:387:2: ( INTEGRAL_LITERAL | REAL_LITERAL )
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:
                pass 
                if self.input.LA(1) in {INTEGRAL_LITERAL, REAL_LITERAL}:
                    self.input.consume()
                    self._state.errorRecovery = False


                else:
                    mse = MismatchedSetException(None, self.input)
                    raise mse





                retval.stop = self.input.LT(-1)



            except RecognitionException as re:
                self.reportError(re)
                self.recover(self.input, re)

        finally:
            pass
        return retval

    # $ANTLR end "numeric_literal"



 

    FOLLOW_36_in_function_block_declaration66 = frozenset([8, 54, 55, 56])
    FOLLOW_function_block_type_in_function_block_declaration68 = frozenset([8])
    FOLLOW_IDENTIFIER_in_function_block_declaration73 = frozenset([30, 32, 37, 48, 51, 52])
    FOLLOW_fb_io_var_declarations_in_function_block_declaration85 = frozenset([30, 32, 37, 48, 51, 52])
    FOLLOW_function_block_body_in_function_block_declaration99 = frozenset([32])
    FOLLOW_32_in_function_block_declaration106 = frozenset([])
    FOLLOW_EOF_in_function_block_declaration122 = frozenset([1])
    FOLLOW_input_declarations_in_fb_io_var_declarations142 = frozenset([1])
    FOLLOW_output_declarations_in_fb_io_var_declarations147 = frozenset([1])
    FOLLOW_51_in_input_declarations159 = frozenset([8])
    FOLLOW_variable_declaration_in_input_declarations163 = frozenset([8, 35])
    FOLLOW_35_in_input_declarations168 = frozenset([1])
    FOLLOW_52_in_output_declarations180 = frozenset([8, 46])
    FOLLOW_46_in_output_declarations182 = frozenset([8])
    FOLLOW_variable_declaration_in_output_declarations187 = frozenset([8, 35])
    FOLLOW_35_in_output_declarations192 = frozenset([1])
    FOLLOW_IDENTIFIER_in_variable_declaration208 = frozenset([23])
    FOLLOW_23_in_variable_declaration210 = frozenset([8, 45])
    FOLLOW_type_in_variable_declaration212 = frozenset([24])
    FOLLOW_24_in_variable_declaration214 = frozenset([1])
    FOLLOW_fuzzify_block_in_function_block_body250 = frozenset([1, 30, 37, 48])
    FOLLOW_defuzzify_block_in_function_block_body255 = frozenset([1, 30, 48])
    FOLLOW_rule_block_in_function_block_body263 = frozenset([1, 48])
    FOLLOW_48_in_rule_block285 = frozenset([8])
    FOLLOW_IDENTIFIER_in_rule_block289 = frozenset([28, 43])
    FOLLOW_operator_definition_in_rule_block295 = frozenset([26, 27])
    FOLLOW_activation_method_in_rule_block301 = frozenset([26])
    FOLLOW_accumulation_method_in_rule_block308 = frozenset([34, 47])
    FOLLOW_rule_in_rule_block331 = frozenset([34, 47])
    FOLLOW_34_in_rule_block341 = frozenset([1])
    FOLLOW_43_in_operator_definition358 = frozenset([23])
    FOLLOW_23_in_operator_definition360 = frozenset([8])
    FOLLOW_IDENTIFIER_in_operator_definition364 = frozenset([24])
    FOLLOW_24_in_operator_definition366 = frozenset([1, 28, 42])
    FOLLOW_28_in_operator_definition370 = frozenset([23])
    FOLLOW_23_in_operator_definition372 = frozenset([8])
    FOLLOW_IDENTIFIER_in_operator_definition376 = frozenset([24])
    FOLLOW_24_in_operator_definition378 = frozenset([1, 42])
    FOLLOW_28_in_operator_definition389 = frozenset([23])
    FOLLOW_23_in_operator_definition391 = frozenset([8])
    FOLLOW_IDENTIFIER_in_operator_definition395 = frozenset([24])
    FOLLOW_24_in_operator_definition397 = frozenset([1, 42, 43])
    FOLLOW_43_in_operator_definition401 = frozenset([23])
    FOLLOW_23_in_operator_definition403 = frozenset([8])
    FOLLOW_IDENTIFIER_in_operator_definition407 = frozenset([24])
    FOLLOW_24_in_operator_definition409 = frozenset([1, 42])
    FOLLOW_42_in_operator_definition418 = frozenset([23])
    FOLLOW_23_in_operator_definition420 = frozenset([8])
    FOLLOW_IDENTIFIER_in_operator_definition426 = frozenset([24])
    FOLLOW_24_in_operator_definition428 = frozenset([1])
    FOLLOW_27_in_activation_method474 = frozenset([23])
    FOLLOW_23_in_activation_method476 = frozenset([8])
    FOLLOW_IDENTIFIER_in_activation_method480 = frozenset([24])
    FOLLOW_24_in_activation_method482 = frozenset([1])
    FOLLOW_26_in_accumulation_method501 = frozenset([23])
    FOLLOW_23_in_accumulation_method503 = frozenset([8])
    FOLLOW_IDENTIFIER_in_accumulation_method507 = frozenset([24])
    FOLLOW_24_in_accumulation_method509 = frozenset([1])
    FOLLOW_47_in_rule529 = frozenset([9])
    FOLLOW_INTEGRAL_LITERAL_in_rule531 = frozenset([23])
    FOLLOW_23_in_rule533 = frozenset([38])
    FOLLOW_38_in_rule537 = frozenset([8, 14, 42])
    FOLLOW_condition_in_rule541 = frozenset([50])
    FOLLOW_50_in_rule544 = frozenset([8, 9, 12])
    FOLLOW_conclusion_in_rule548 = frozenset([24, 53])
    FOLLOW_53_in_rule551 = frozenset([8, 9, 12])
    FOLLOW_weighting_factor_in_rule555 = frozenset([24])
    FOLLOW_24_in_rule559 = frozenset([1])
    FOLLOW_expr_in_condition580 = frozenset([1])
    FOLLOW_term_in_expr602 = frozenset([1, 43])
    FOLLOW_43_in_expr608 = frozenset([8, 14, 42])
    FOLLOW_expr_in_expr614 = frozenset([1])
    FOLLOW_pred_in_term643 = frozenset([1, 28])
    FOLLOW_42_in_term650 = frozenset([14])
    FOLLOW_14_in_term653 = frozenset([8, 14, 42])
    FOLLOW_expr_in_term657 = frozenset([15])
    FOLLOW_15_in_term660 = frozenset([1, 28])
    FOLLOW_28_in_term667 = frozenset([8, 14, 42])
    FOLLOW_term_in_term672 = frozenset([1])
    FOLLOW_IDENTIFIER_in_pred703 = frozenset([39])
    FOLLOW_39_in_pred705 = frozenset([8, 42])
    FOLLOW_42_in_pred710 = frozenset([8])
    FOLLOW_IDENTIFIER_in_pred716 = frozenset([1])
    FOLLOW_mconclusion_in_conclusion756 = frozenset([1])
    FOLLOW_sconclusion_in_conclusion760 = frozenset([1])
    FOLLOW_IDENTIFIER_in_mconclusion789 = frozenset([20, 39])
    FOLLOW_set_in_mconclusion791 = frozenset([8])
    FOLLOW_IDENTIFIER_in_mconclusion801 = frozenset([1, 18])
    FOLLOW_18_in_mconclusion808 = frozenset([8])
    FOLLOW_IDENTIFIER_in_mconclusion812 = frozenset([20, 39])
    FOLLOW_set_in_mconclusion814 = frozenset([8])
    FOLLOW_IDENTIFIER_in_mconclusion824 = frozenset([1, 18])
    FOLLOW_IDENTIFIER_in_sconclusion847 = frozenset([1, 16, 17, 19, 22])
    FOLLOW_numeric_literal_in_sconclusion853 = frozenset([1, 16, 17, 19, 22])
    FOLLOW_17_in_sconclusion860 = frozenset([8, 9, 12])
    FOLLOW_19_in_sconclusion862 = frozenset([8, 9, 12])
    FOLLOW_16_in_sconclusion864 = frozenset([8, 9, 12, 16])
    FOLLOW_16_in_sconclusion865 = frozenset([8, 9, 12])
    FOLLOW_22_in_sconclusion868 = frozenset([8, 9, 12, 22])
    FOLLOW_22_in_sconclusion869 = frozenset([8, 9, 12])
    FOLLOW_sconclusion_in_sconclusion875 = frozenset([1])
    FOLLOW_IDENTIFIER_in_tconclusion906 = frozenset([20, 39])
    FOLLOW_set_in_tconclusion908 = frozenset([8])
    FOLLOW_IDENTIFIER_in_tconclusion918 = frozenset([1])
    FOLLOW_IDENTIFIER_in_weighting_factor936 = frozenset([1])
    FOLLOW_numeric_literal_in_weighting_factor946 = frozenset([1])
    FOLLOW_37_in_fuzzify_block959 = frozenset([8])
    FOLLOW_IDENTIFIER_in_fuzzify_block963 = frozenset([33, 49])
    FOLLOW_linguistic_term_in_fuzzify_block974 = frozenset([33, 49])
    FOLLOW_33_in_fuzzify_block982 = frozenset([1])
    FOLLOW_30_in_defuzzify_block993 = frozenset([8])
    FOLLOW_IDENTIFIER_in_defuzzify_block997 = frozenset([40, 49])
    FOLLOW_linguistic_term_in_defuzzify_block1006 = frozenset([40, 49])
    FOLLOW_defuzzification_method_in_defuzzify_block1016 = frozenset([29])
    FOLLOW_default_value_in_defuzzify_block1026 = frozenset([31, 44])
    FOLLOW_range_in_defuzzify_block1036 = frozenset([31])
    FOLLOW_31_in_defuzzify_block1041 = frozenset([1])
    FOLLOW_IDENTIFIER_in_variable_name1051 = frozenset([1])
    FOLLOW_49_in_linguistic_term1065 = frozenset([8])
    FOLLOW_IDENTIFIER_in_linguistic_term1069 = frozenset([23])
    FOLLOW_23_in_linguistic_term1071 = frozenset([25])
    FOLLOW_25_in_linguistic_term1072 = frozenset([8, 9, 12, 14])
    FOLLOW_membership_function_in_linguistic_term1076 = frozenset([24])
    FOLLOW_24_in_linguistic_term1078 = frozenset([1])
    FOLLOW_IDENTIFIER_in_term_name1100 = frozenset([1])
    FOLLOW_singleton_in_membership_function1119 = frozenset([1])
    FOLLOW_points_in_membership_function1123 = frozenset([1])
    FOLLOW_other_function_in_membership_function1127 = frozenset([1])
    FOLLOW_numeric_literal_in_singleton1149 = frozenset([1])
    FOLLOW_variable_name_in_singleton1164 = frozenset([1])
    FOLLOW_14_in_points1187 = frozenset([8, 9, 12])
    FOLLOW_numeric_literal_in_points1192 = frozenset([18])
    FOLLOW_variable_name_in_points1194 = frozenset([18])
    FOLLOW_18_in_points1197 = frozenset([9, 12])
    FOLLOW_numeric_literal_in_points1201 = frozenset([15])
    FOLLOW_15_in_points1203 = frozenset([1, 14])
    FOLLOW_40_in_defuzzification_method1231 = frozenset([23])
    FOLLOW_23_in_defuzzification_method1233 = frozenset([8])
    FOLLOW_IDENTIFIER_in_defuzzification_method1237 = frozenset([24])
    FOLLOW_24_in_defuzzification_method1239 = frozenset([1])
    FOLLOW_IDENTIFIER_in_other_function1263 = frozenset([14])
    FOLLOW_14_in_other_function1267 = frozenset([9, 12, 14, 15])
    FOLLOW_function_param_in_other_function1276 = frozenset([15, 18])
    FOLLOW_18_in_other_function1283 = frozenset([9, 12, 14])
    FOLLOW_function_param_in_other_function1287 = frozenset([15, 18])
    FOLLOW_15_in_other_function1300 = frozenset([1])
    FOLLOW_numeric_literal_in_function_param1321 = frozenset([1])
    FOLLOW_14_in_function_param1331 = frozenset([9, 12])
    FOLLOW_numeric_literal_in_function_param1335 = frozenset([18])
    FOLLOW_18_in_function_param1337 = frozenset([9, 12])
    FOLLOW_numeric_literal_in_function_param1341 = frozenset([15])
    FOLLOW_15_in_function_param1343 = frozenset([1])
    FOLLOW_29_in_default_value1367 = frozenset([23])
    FOLLOW_23_in_default_value1369 = frozenset([25])
    FOLLOW_25_in_default_value1370 = frozenset([9, 12, 41])
    FOLLOW_numeric_literal_in_default_value1377 = frozenset([24])
    FOLLOW_41_in_default_value1387 = frozenset([24])
    FOLLOW_24_in_default_value1392 = frozenset([1])
    FOLLOW_44_in_range1406 = frozenset([23])
    FOLLOW_23_in_range1408 = frozenset([25])
    FOLLOW_25_in_range1409 = frozenset([14])
    FOLLOW_14_in_range1411 = frozenset([9, 12])
    FOLLOW_numeric_literal_in_range1415 = frozenset([21])
    FOLLOW_21_in_range1417 = frozenset([9, 12])
    FOLLOW_numeric_literal_in_range1421 = frozenset([15])
    FOLLOW_15_in_range1423 = frozenset([24])
    FOLLOW_24_in_range1425 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("FCLLexer", FCLParser)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
