# $ANTLR 3.5 C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g 2013-06-21 00:01:51

import sys
from antlr3 import *


#!/usr/bin/python3



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

class FCLLexer(Lexer):

    grammarFileName = "C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g"
    api_version = 1

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super().__init__(input, state)

        self.delegates = []

        self.dfa14 = self.DFA14(
            self, 14,
            eot = self.DFA14_eot,
            eof = self.DFA14_eof,
            min = self.DFA14_min,
            max = self.DFA14_max,
            accept = self.DFA14_accept,
            special = self.DFA14_special,
            transition = self.DFA14_transition
            )

        self.dfa18 = self.DFA18(
            self, 18,
            eot = self.DFA18_eot,
            eof = self.DFA18_eof,
            min = self.DFA18_min,
            max = self.DFA18_max,
            accept = self.DFA18_accept,
            special = self.DFA18_special,
            transition = self.DFA18_transition
            )






    # $ANTLR start "T__14"
    def mT__14(self, ):
        try:
            _type = T__14
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:11:7: ( '(' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:11:9: '('
            pass 
            self.match('(')



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__14"



    # $ANTLR start "T__15"
    def mT__15(self, ):
        try:
            _type = T__15
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:12:7: ( ')' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:12:9: ')'
            pass 
            self.match(')')



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__15"



    # $ANTLR start "T__16"
    def mT__16(self, ):
        try:
            _type = T__16
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:13:7: ( '*' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:13:9: '*'
            pass 
            self.match('*')



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__16"



    # $ANTLR start "T__17"
    def mT__17(self, ):
        try:
            _type = T__17
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:14:7: ( '+' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:14:9: '+'
            pass 
            self.match('+')



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__17"



    # $ANTLR start "T__18"
    def mT__18(self, ):
        try:
            _type = T__18
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:15:7: ( ',' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:15:9: ','
            pass 
            self.match(',')



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__18"



    # $ANTLR start "T__19"
    def mT__19(self, ):
        try:
            _type = T__19
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:16:7: ( '-' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:16:9: '-'
            pass 
            self.match('-')



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__19"



    # $ANTLR start "T__20"
    def mT__20(self, ):
        try:
            _type = T__20
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:17:7: ( '.' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:17:9: '.'
            pass 
            self.match('.')



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__20"



    # $ANTLR start "T__21"
    def mT__21(self, ):
        try:
            _type = T__21
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:18:7: ( '..' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:18:9: '..'
            pass 
            self.match("..")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__21"



    # $ANTLR start "T__22"
    def mT__22(self, ):
        try:
            _type = T__22
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:19:7: ( '/' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:19:9: '/'
            pass 
            self.match('/')



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__22"



    # $ANTLR start "T__23"
    def mT__23(self, ):
        try:
            _type = T__23
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:20:7: ( ':' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:20:9: ':'
            pass 
            self.match(':')



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__23"



    # $ANTLR start "T__24"
    def mT__24(self, ):
        try:
            _type = T__24
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:21:7: ( ';' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:21:9: ';'
            pass 
            self.match(';')



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__24"



    # $ANTLR start "T__25"
    def mT__25(self, ):
        try:
            _type = T__25
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:22:7: ( '=' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:22:9: '='
            pass 
            self.match('=')



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__25"



    # $ANTLR start "T__26"
    def mT__26(self, ):
        try:
            _type = T__26
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:23:7: ( 'ACCU' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:23:9: 'ACCU'
            pass 
            self.match("ACCU")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__26"



    # $ANTLR start "T__27"
    def mT__27(self, ):
        try:
            _type = T__27
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:24:7: ( 'ACT' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:24:9: 'ACT'
            pass 
            self.match("ACT")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__27"



    # $ANTLR start "T__28"
    def mT__28(self, ):
        try:
            _type = T__28
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:25:7: ( 'AND' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:25:9: 'AND'
            pass 
            self.match("AND")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__28"



    # $ANTLR start "T__29"
    def mT__29(self, ):
        try:
            _type = T__29
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:26:7: ( 'DEFAULT' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:26:9: 'DEFAULT'
            pass 
            self.match("DEFAULT")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__29"



    # $ANTLR start "T__30"
    def mT__30(self, ):
        try:
            _type = T__30
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:27:7: ( 'DEFUZZIFY' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:27:9: 'DEFUZZIFY'
            pass 
            self.match("DEFUZZIFY")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__30"



    # $ANTLR start "T__31"
    def mT__31(self, ):
        try:
            _type = T__31
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:28:7: ( 'END_DEFUZZIFY' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:28:9: 'END_DEFUZZIFY'
            pass 
            self.match("END_DEFUZZIFY")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__31"



    # $ANTLR start "T__32"
    def mT__32(self, ):
        try:
            _type = T__32
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:29:7: ( 'END_FUNCTION_BLOCK' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:29:9: 'END_FUNCTION_BLOCK'
            pass 
            self.match("END_FUNCTION_BLOCK")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__32"



    # $ANTLR start "T__33"
    def mT__33(self, ):
        try:
            _type = T__33
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:30:7: ( 'END_FUZZIFY' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:30:9: 'END_FUZZIFY'
            pass 
            self.match("END_FUZZIFY")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__33"



    # $ANTLR start "T__34"
    def mT__34(self, ):
        try:
            _type = T__34
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:31:7: ( 'END_RULEBLOCK' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:31:9: 'END_RULEBLOCK'
            pass 
            self.match("END_RULEBLOCK")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__34"



    # $ANTLR start "T__35"
    def mT__35(self, ):
        try:
            _type = T__35
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:32:7: ( 'END_VAR' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:32:9: 'END_VAR'
            pass 
            self.match("END_VAR")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__35"



    # $ANTLR start "T__36"
    def mT__36(self, ):
        try:
            _type = T__36
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:33:7: ( 'FUNCTION_BLOCK' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:33:9: 'FUNCTION_BLOCK'
            pass 
            self.match("FUNCTION_BLOCK")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__36"



    # $ANTLR start "T__37"
    def mT__37(self, ):
        try:
            _type = T__37
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:34:7: ( 'FUZZIFY' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:34:9: 'FUZZIFY'
            pass 
            self.match("FUZZIFY")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__37"



    # $ANTLR start "T__38"
    def mT__38(self, ):
        try:
            _type = T__38
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:35:7: ( 'IF' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:35:9: 'IF'
            pass 
            self.match("IF")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__38"



    # $ANTLR start "T__39"
    def mT__39(self, ):
        try:
            _type = T__39
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:36:7: ( 'IS' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:36:9: 'IS'
            pass 
            self.match("IS")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__39"



    # $ANTLR start "T__40"
    def mT__40(self, ):
        try:
            _type = T__40
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:37:7: ( 'METHOD' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:37:9: 'METHOD'
            pass 
            self.match("METHOD")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__40"



    # $ANTLR start "T__41"
    def mT__41(self, ):
        try:
            _type = T__41
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:38:7: ( 'NC' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:38:9: 'NC'
            pass 
            self.match("NC")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__41"



    # $ANTLR start "T__42"
    def mT__42(self, ):
        try:
            _type = T__42
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:39:7: ( 'NOT' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:39:9: 'NOT'
            pass 
            self.match("NOT")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__42"



    # $ANTLR start "T__43"
    def mT__43(self, ):
        try:
            _type = T__43
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:40:7: ( 'OR' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:40:9: 'OR'
            pass 
            self.match("OR")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__43"



    # $ANTLR start "T__44"
    def mT__44(self, ):
        try:
            _type = T__44
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:41:7: ( 'RANGE' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:41:9: 'RANGE'
            pass 
            self.match("RANGE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__44"



    # $ANTLR start "T__45"
    def mT__45(self, ):
        try:
            _type = T__45
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:42:7: ( 'REAL' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:42:9: 'REAL'
            pass 
            self.match("REAL")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__45"



    # $ANTLR start "T__46"
    def mT__46(self, ):
        try:
            _type = T__46
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:43:7: ( 'RETAIN' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:43:9: 'RETAIN'
            pass 
            self.match("RETAIN")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__46"



    # $ANTLR start "T__47"
    def mT__47(self, ):
        try:
            _type = T__47
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:44:7: ( 'RULE' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:44:9: 'RULE'
            pass 
            self.match("RULE")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__47"



    # $ANTLR start "T__48"
    def mT__48(self, ):
        try:
            _type = T__48
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:45:7: ( 'RULEBLOCK' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:45:9: 'RULEBLOCK'
            pass 
            self.match("RULEBLOCK")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__48"



    # $ANTLR start "T__49"
    def mT__49(self, ):
        try:
            _type = T__49
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:46:7: ( 'TERM' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:46:9: 'TERM'
            pass 
            self.match("TERM")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__49"



    # $ANTLR start "T__50"
    def mT__50(self, ):
        try:
            _type = T__50
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:47:7: ( 'THEN' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:47:9: 'THEN'
            pass 
            self.match("THEN")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__50"



    # $ANTLR start "T__51"
    def mT__51(self, ):
        try:
            _type = T__51
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:48:7: ( 'VAR_INPUT' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:48:9: 'VAR_INPUT'
            pass 
            self.match("VAR_INPUT")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__51"



    # $ANTLR start "T__52"
    def mT__52(self, ):
        try:
            _type = T__52
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:49:7: ( 'VAR_OUTPUT' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:49:9: 'VAR_OUTPUT'
            pass 
            self.match("VAR_OUTPUT")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__52"



    # $ANTLR start "T__53"
    def mT__53(self, ):
        try:
            _type = T__53
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:50:7: ( 'WITH' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:50:9: 'WITH'
            pass 
            self.match("WITH")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__53"



    # $ANTLR start "T__54"
    def mT__54(self, ):
        try:
            _type = T__54
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:51:7: ( '_MAMDAMI_' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:51:9: '_MAMDAMI_'
            pass 
            self.match("_MAMDAMI_")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__54"



    # $ANTLR start "T__55"
    def mT__55(self, ):
        try:
            _type = T__55
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:52:7: ( '_SUGENO_' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:52:9: '_SUGENO_'
            pass 
            self.match("_SUGENO_")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__55"



    # $ANTLR start "T__56"
    def mT__56(self, ):
        try:
            _type = T__56
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:53:7: ( '_TSUKAMOTO_' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:53:9: '_TSUKAMOTO_'
            pass 
            self.match("_TSUKAMOTO_")




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "T__56"



    # $ANTLR start "IDENTIFIER"
    def mIDENTIFIER(self, ):
        try:
            _type = IDENTIFIER
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:396:13: ( LETTER ( LETTER_ | DIGIT )* )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:396:15: LETTER ( LETTER_ | DIGIT )*
            pass 
            self.mLETTER()


            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:396:22: ( LETTER_ | DIGIT )*
            while True: #loop1
                alt1 = 3
                LA1_0 = self.input.LT(1)

                if (('A' <= LA1_0 <= 'Z') or ('a' <= LA1_0 <= 'z') or LA1_0 in {'_'}) :
                    alt1 = 1
                elif (('0' <= LA1_0 <= '9') or LA1_0 in {}) :
                    alt1 = 2


                if alt1 == 1:
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:396:23: LETTER_
                    pass 
                    self.mLETTER_()



                elif alt1 == 2:
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:396:33: DIGIT
                    pass 
                    self.mDIGIT()



                else:
                    break #loop1




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "IDENTIFIER"



    # $ANTLR start "LETTER"
    def mLETTER(self, ):
        try:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:398:17: ( 'a' .. 'z' | 'A' .. 'Z' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:
            pass 
            if ('A' <= self.input.LT(1) <= 'Z') or ('a' <= self.input.LT(1) <= 'z') or self.input.LT(1) in {}:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse






        finally:
            pass

    # $ANTLR end "LETTER"



    # $ANTLR start "LETTER_"
    def mLETTER_(self, ):
        try:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:399:18: ( 'a' .. 'z' | 'A' .. 'Z' | '_' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:
            pass 
            if ('A' <= self.input.LT(1) <= 'Z') or ('a' <= self.input.LT(1) <= 'z') or self.input.LT(1) in {'_'}:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse






        finally:
            pass

    # $ANTLR end "LETTER_"



    # $ANTLR start "REAL_LITERAL"
    def mREAL_LITERAL(self, ):
        try:
            _type = REAL_LITERAL
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:401:14: ( ( '+' | '-' )? ( DIGIT )+ '.' ( DIGIT )+ )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:401:16: ( '+' | '-' )? ( DIGIT )+ '.' ( DIGIT )+
            pass 
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:401:16: ( '+' | '-' )?
            alt2 = 2
            LA2_0 = self.input.LT(1)

            if (LA2_0 in {'+', '-'}) :
                alt2 = 1
            if alt2 == 1:
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:
                pass 
                if self.input.LT(1) in {'+', '-'}:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse






            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:401:27: ( DIGIT )+
            cnt3 = 0
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LT(1)

                if (('0' <= LA3_0 <= '9') or LA3_0 in {}) :
                    alt3 = 1


                if alt3 == 1:
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:401:27: DIGIT
                    pass 
                    self.mDIGIT()



                else:
                    if cnt3 >= 1:
                        break #loop3

                    eee = EarlyExitException(3, self.input)
                    raise eee

                cnt3 += 1


            self.match('.')

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:401:39: ( DIGIT )+
            cnt4 = 0
            while True: #loop4
                alt4 = 2
                LA4_0 = self.input.LT(1)

                if (('0' <= LA4_0 <= '9') or LA4_0 in {}) :
                    alt4 = 1


                if alt4 == 1:
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:401:39: DIGIT
                    pass 
                    self.mDIGIT()



                else:
                    if cnt4 >= 1:
                        break #loop4

                    eee = EarlyExitException(4, self.input)
                    raise eee

                cnt4 += 1




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "REAL_LITERAL"



    # $ANTLR start "INTEGRAL_LITERAL"
    def mINTEGRAL_LITERAL(self, ):
        try:
            _type = INTEGRAL_LITERAL
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:403:18: ( ( '+' | '-' )? ( '0' .. '9' )+ )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:403:20: ( '+' | '-' )? ( '0' .. '9' )+
            pass 
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:403:20: ( '+' | '-' )?
            alt5 = 2
            LA5_0 = self.input.LT(1)

            if (LA5_0 in {'+', '-'}) :
                alt5 = 1
            if alt5 == 1:
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:
                pass 
                if self.input.LT(1) in {'+', '-'}:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse






            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:403:31: ( '0' .. '9' )+
            cnt6 = 0
            while True: #loop6
                alt6 = 2
                LA6_0 = self.input.LT(1)

                if (('0' <= LA6_0 <= '9') or LA6_0 in {}) :
                    alt6 = 1


                if alt6 == 1:
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:
                    pass 
                    if ('0' <= self.input.LT(1) <= '9') or self.input.LT(1) in {}:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt6 >= 1:
                        break #loop6

                    eee = EarlyExitException(6, self.input)
                    raise eee

                cnt6 += 1




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "INTEGRAL_LITERAL"



    # $ANTLR start "DIGIT"
    def mDIGIT(self, ):
        try:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:404:16: ( ( '0' .. '9' )+ )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:404:18: ( '0' .. '9' )+
            pass 
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:404:18: ( '0' .. '9' )+
            cnt7 = 0
            while True: #loop7
                alt7 = 2
                LA7_0 = self.input.LT(1)

                if (('0' <= LA7_0 <= '9') or LA7_0 in {}) :
                    alt7 = 1


                if alt7 == 1:
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:
                    pass 
                    if ('0' <= self.input.LT(1) <= '9') or self.input.LT(1) in {}:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt7 >= 1:
                        break #loop7

                    eee = EarlyExitException(7, self.input)
                    raise eee

                cnt7 += 1





        finally:
            pass

    # $ANTLR end "DIGIT"



    # $ANTLR start "FLOAT"
    def mFLOAT(self, ):
        try:
            _type = FLOAT
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:407:5: ( ( '0' .. '9' )+ '.' ( '0' .. '9' )* ( EXPONENT )? | '.' ( '0' .. '9' )+ ( EXPONENT )? | ( '0' .. '9' )+ EXPONENT )
            alt14 = 3
            alt14 = self.dfa14.predict(self.input)
            if alt14 == 1:
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:407:9: ( '0' .. '9' )+ '.' ( '0' .. '9' )* ( EXPONENT )?
                pass 
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:407:9: ( '0' .. '9' )+
                cnt8 = 0
                while True: #loop8
                    alt8 = 2
                    LA8_0 = self.input.LT(1)

                    if (('0' <= LA8_0 <= '9') or LA8_0 in {}) :
                        alt8 = 1


                    if alt8 == 1:
                        # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:
                        pass 
                        if ('0' <= self.input.LT(1) <= '9') or self.input.LT(1) in {}:
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        if cnt8 >= 1:
                            break #loop8

                        eee = EarlyExitException(8, self.input)
                        raise eee

                    cnt8 += 1


                self.match('.')

                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:407:25: ( '0' .. '9' )*
                while True: #loop9
                    alt9 = 2
                    LA9_0 = self.input.LT(1)

                    if (('0' <= LA9_0 <= '9') or LA9_0 in {}) :
                        alt9 = 1


                    if alt9 == 1:
                        # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:
                        pass 
                        if ('0' <= self.input.LT(1) <= '9') or self.input.LT(1) in {}:
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        break #loop9


                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:407:37: ( EXPONENT )?
                alt10 = 2
                LA10_0 = self.input.LT(1)

                if (LA10_0 in {'E', 'e'}) :
                    alt10 = 1
                if alt10 == 1:
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:407:37: EXPONENT
                    pass 
                    self.mEXPONENT()






            elif alt14 == 2:
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:408:9: '.' ( '0' .. '9' )+ ( EXPONENT )?
                pass 
                self.match('.')

                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:408:13: ( '0' .. '9' )+
                cnt11 = 0
                while True: #loop11
                    alt11 = 2
                    LA11_0 = self.input.LT(1)

                    if (('0' <= LA11_0 <= '9') or LA11_0 in {}) :
                        alt11 = 1


                    if alt11 == 1:
                        # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:
                        pass 
                        if ('0' <= self.input.LT(1) <= '9') or self.input.LT(1) in {}:
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        if cnt11 >= 1:
                            break #loop11

                        eee = EarlyExitException(11, self.input)
                        raise eee

                    cnt11 += 1


                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:408:25: ( EXPONENT )?
                alt12 = 2
                LA12_0 = self.input.LT(1)

                if (LA12_0 in {'E', 'e'}) :
                    alt12 = 1
                if alt12 == 1:
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:408:25: EXPONENT
                    pass 
                    self.mEXPONENT()






            elif alt14 == 3:
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:409:9: ( '0' .. '9' )+ EXPONENT
                pass 
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:409:9: ( '0' .. '9' )+
                cnt13 = 0
                while True: #loop13
                    alt13 = 2
                    LA13_0 = self.input.LT(1)

                    if (('0' <= LA13_0 <= '9') or LA13_0 in {}) :
                        alt13 = 1


                    if alt13 == 1:
                        # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:
                        pass 
                        if ('0' <= self.input.LT(1) <= '9') or self.input.LT(1) in {}:
                            self.input.consume()
                        else:
                            mse = MismatchedSetException(None, self.input)
                            self.recover(mse)
                            raise mse




                    else:
                        if cnt13 >= 1:
                            break #loop13

                        eee = EarlyExitException(13, self.input)
                        raise eee

                    cnt13 += 1


                self.mEXPONENT()



            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "FLOAT"



    # $ANTLR start "COMMENT"
    def mCOMMENT(self, ):
        try:
            _type = COMMENT
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:412:12: ( '(*' ( options {greedy=false; } : . )* '*)' )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:412:16: '(*' ( options {greedy=false; } : . )* '*)'
            pass 
            self.match("(*")


            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:412:21: ( options {greedy=false; } : . )*
            while True: #loop15
                alt15 = 2
                LA15_0 = self.input.LT(1)

                if (LA15_0 == '*') :
                    LA15_1 = self.input.LT(2)

                    if (LA15_1 == ')') :
                        alt15 = 2
                    elif (('\u0000' <= LA15_1 <= '(') or ('*' <= LA15_1 <= '\uFFFF') or LA15_1 in {}) :
                        alt15 = 1


                elif (('\u0000' <= LA15_0 <= ')') or ('+' <= LA15_0 <= '\uFFFF') or LA15_0 in {}) :
                    alt15 = 1


                if alt15 == 1:
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:412:49: .
                    pass 
                    self.matchAny()


                else:
                    break #loop15


            self.match("*)")


            #action start
            _channel=HIDDEN;
            #action end




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "COMMENT"



    # $ANTLR start "WS"
    def mWS(self, ):
        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:414:5: ( ( ' ' | '\\t' | '\\r' | '\\n' ) )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:414:9: ( ' ' | '\\t' | '\\r' | '\\n' )
            pass 
            if self.input.LT(1) in {'\t', '\n', '\r', ' '}:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            #action start
            _channel=HIDDEN;
            #action end




            self._state.type = _type
            self._state.channel = _channel
        finally:
            pass

    # $ANTLR end "WS"



    # $ANTLR start "EXPONENT"
    def mEXPONENT(self, ):
        try:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:423:10: ( ( 'e' | 'E' ) ( '+' | '-' )? ( '0' .. '9' )+ )
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:423:12: ( 'e' | 'E' ) ( '+' | '-' )? ( '0' .. '9' )+
            pass 
            if self.input.LT(1) in {'E', 'e'}:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse



            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:423:22: ( '+' | '-' )?
            alt16 = 2
            LA16_0 = self.input.LT(1)

            if (LA16_0 in {'+', '-'}) :
                alt16 = 1
            if alt16 == 1:
                # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:
                pass 
                if self.input.LT(1) in {'+', '-'}:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse






            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:423:33: ( '0' .. '9' )+
            cnt17 = 0
            while True: #loop17
                alt17 = 2
                LA17_0 = self.input.LT(1)

                if (('0' <= LA17_0 <= '9') or LA17_0 in {}) :
                    alt17 = 1


                if alt17 == 1:
                    # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:
                    pass 
                    if ('0' <= self.input.LT(1) <= '9') or self.input.LT(1) in {}:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse




                else:
                    if cnt17 >= 1:
                        break #loop17

                    eee = EarlyExitException(17, self.input)
                    raise eee

                cnt17 += 1





        finally:
            pass

    # $ANTLR end "EXPONENT"



    def mTokens(self):
        # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:8: ( T__14 | T__15 | T__16 | T__17 | T__18 | T__19 | T__20 | T__21 | T__22 | T__23 | T__24 | T__25 | T__26 | T__27 | T__28 | T__29 | T__30 | T__31 | T__32 | T__33 | T__34 | T__35 | T__36 | T__37 | T__38 | T__39 | T__40 | T__41 | T__42 | T__43 | T__44 | T__45 | T__46 | T__47 | T__48 | T__49 | T__50 | T__51 | T__52 | T__53 | T__54 | T__55 | T__56 | IDENTIFIER | REAL_LITERAL | INTEGRAL_LITERAL | FLOAT | COMMENT | WS )
        alt18 = 49
        alt18 = self.dfa18.predict(self.input)
        if alt18 == 1:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:10: T__14
            pass 
            self.mT__14()



        elif alt18 == 2:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:16: T__15
            pass 
            self.mT__15()



        elif alt18 == 3:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:22: T__16
            pass 
            self.mT__16()



        elif alt18 == 4:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:28: T__17
            pass 
            self.mT__17()



        elif alt18 == 5:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:34: T__18
            pass 
            self.mT__18()



        elif alt18 == 6:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:40: T__19
            pass 
            self.mT__19()



        elif alt18 == 7:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:46: T__20
            pass 
            self.mT__20()



        elif alt18 == 8:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:52: T__21
            pass 
            self.mT__21()



        elif alt18 == 9:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:58: T__22
            pass 
            self.mT__22()



        elif alt18 == 10:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:64: T__23
            pass 
            self.mT__23()



        elif alt18 == 11:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:70: T__24
            pass 
            self.mT__24()



        elif alt18 == 12:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:76: T__25
            pass 
            self.mT__25()



        elif alt18 == 13:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:82: T__26
            pass 
            self.mT__26()



        elif alt18 == 14:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:88: T__27
            pass 
            self.mT__27()



        elif alt18 == 15:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:94: T__28
            pass 
            self.mT__28()



        elif alt18 == 16:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:100: T__29
            pass 
            self.mT__29()



        elif alt18 == 17:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:106: T__30
            pass 
            self.mT__30()



        elif alt18 == 18:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:112: T__31
            pass 
            self.mT__31()



        elif alt18 == 19:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:118: T__32
            pass 
            self.mT__32()



        elif alt18 == 20:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:124: T__33
            pass 
            self.mT__33()



        elif alt18 == 21:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:130: T__34
            pass 
            self.mT__34()



        elif alt18 == 22:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:136: T__35
            pass 
            self.mT__35()



        elif alt18 == 23:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:142: T__36
            pass 
            self.mT__36()



        elif alt18 == 24:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:148: T__37
            pass 
            self.mT__37()



        elif alt18 == 25:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:154: T__38
            pass 
            self.mT__38()



        elif alt18 == 26:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:160: T__39
            pass 
            self.mT__39()



        elif alt18 == 27:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:166: T__40
            pass 
            self.mT__40()



        elif alt18 == 28:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:172: T__41
            pass 
            self.mT__41()



        elif alt18 == 29:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:178: T__42
            pass 
            self.mT__42()



        elif alt18 == 30:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:184: T__43
            pass 
            self.mT__43()



        elif alt18 == 31:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:190: T__44
            pass 
            self.mT__44()



        elif alt18 == 32:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:196: T__45
            pass 
            self.mT__45()



        elif alt18 == 33:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:202: T__46
            pass 
            self.mT__46()



        elif alt18 == 34:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:208: T__47
            pass 
            self.mT__47()



        elif alt18 == 35:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:214: T__48
            pass 
            self.mT__48()



        elif alt18 == 36:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:220: T__49
            pass 
            self.mT__49()



        elif alt18 == 37:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:226: T__50
            pass 
            self.mT__50()



        elif alt18 == 38:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:232: T__51
            pass 
            self.mT__51()



        elif alt18 == 39:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:238: T__52
            pass 
            self.mT__52()



        elif alt18 == 40:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:244: T__53
            pass 
            self.mT__53()



        elif alt18 == 41:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:250: T__54
            pass 
            self.mT__54()



        elif alt18 == 42:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:256: T__55
            pass 
            self.mT__55()



        elif alt18 == 43:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:262: T__56
            pass 
            self.mT__56()



        elif alt18 == 44:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:268: IDENTIFIER
            pass 
            self.mIDENTIFIER()



        elif alt18 == 45:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:279: REAL_LITERAL
            pass 
            self.mREAL_LITERAL()



        elif alt18 == 46:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:292: INTEGRAL_LITERAL
            pass 
            self.mINTEGRAL_LITERAL()



        elif alt18 == 47:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:309: FLOAT
            pass 
            self.mFLOAT()



        elif alt18 == 48:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:315: COMMENT
            pass 
            self.mCOMMENT()



        elif alt18 == 49:
            # C:\\Users\\CL\\PycharmProjects\\fuzzython\\store\\FCL.g:1:323: WS
            pass 
            self.mWS()








    # lookup tables for DFA #14

    DFA14_eot = DFA.unpack(
        "\5\uffff"
        )

    DFA14_eof = DFA.unpack(
        "\5\uffff"
        )

    DFA14_min = DFA.unpack(
        "\2\56\3\uffff"
        )

    DFA14_max = DFA.unpack(
        "\1\71\1\145\3\uffff"
        )

    DFA14_accept = DFA.unpack(
        "\2\uffff\1\2\1\1\1\3"
        )

    DFA14_special = DFA.unpack(
        "\5\uffff"
        )


    DFA14_transition = [
        DFA.unpack("\1\2\1\uffff\12\1"),
        DFA.unpack("\1\3\1\uffff\12\1\13\uffff\1\4\37\uffff\1\4"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("")
    ]

    # class definition for DFA #14

    class DFA14(DFA):
        pass


    # lookup tables for DFA #18

    DFA18_eot = DFA.unpack(
        "\1\uffff\1\35\2\uffff\1\36\1\uffff\1\40\1\42\4\uffff\14\31\2\uffff"
        "\1\71\4\uffff\1\71\4\uffff\5\31\1\103\1\104\1\31\1\106\1\31\1\110"
        "\7\31\4\uffff\1\43\1\uffff\1\31\1\123\1\124\4\31\2\uffff\1\31\1"
        "\uffff\1\133\1\uffff\10\31\1\73\1\144\2\uffff\6\31\1\uffff\1\31"
        "\1\157\1\31\1\162\1\163\1\164\1\31\1\167\1\uffff\11\31\1\u0081\1"
        "\uffff\2\31\3\uffff\2\31\1\uffff\10\31\1\u008f\1\uffff\1\u0090\3"
        "\31\1\u0094\5\31\1\u009a\1\31\1\u009c\2\uffff\3\31\1\uffff\5\31"
        "\1\uffff\1\31\1\uffff\3\31\1\u00a9\5\31\1\u00af\1\u00b0\1\31\1\uffff"
        "\5\31\2\uffff\1\u00b7\2\31\1\u00ba\2\31\1\uffff\2\31\1\uffff\2\31"
        "\1\u00c1\1\31\1\u00c3\1\31\1\uffff\1\31\1\uffff\1\u00c6\1\31\1\uffff"
        "\2\31\1\u00ca\1\uffff"
        )

    DFA18_eof = DFA.unpack(
        "\u00cb\uffff"
        )

    DFA18_min = DFA.unpack(
        "\1\11\1\52\2\uffff\1\60\1\uffff\1\60\1\56\4\uffff\1\103\1\105\1"
        "\116\1\125\1\106\1\105\1\103\1\122\1\101\1\105\1\101\1\111\1\115"
        "\1\uffff\1\56\4\uffff\1\56\4\uffff\1\103\1\104\1\106\1\104\1\116"
        "\2\60\1\124\1\60\1\124\1\60\1\116\1\101\1\114\1\122\1\105\1\122"
        "\1\124\4\uffff\1\60\1\uffff\1\125\2\60\1\101\1\137\1\103\1\132\2"
        "\uffff\1\110\1\uffff\1\60\1\uffff\1\107\1\114\1\101\1\105\1\115"
        "\1\116\1\137\1\110\2\60\2\uffff\1\125\1\132\1\104\1\124\1\111\1"
        "\117\1\uffff\1\105\1\60\1\111\3\60\1\111\1\60\1\uffff\1\114\1\132"
        "\1\105\2\125\1\101\1\111\1\106\1\104\1\60\1\uffff\1\116\1\114\3"
        "\uffff\1\116\1\125\1\uffff\1\124\1\111\1\106\1\116\1\114\1\122\1"
        "\117\1\131\1\60\1\uffff\1\60\1\117\1\120\1\124\1\60\1\106\1\125"
        "\1\103\1\132\1\105\1\60\1\116\1\60\2\uffff\1\103\1\125\1\120\1\uffff"
        "\1\131\1\132\1\124\1\111\1\102\1\uffff\1\137\1\uffff\1\113\1\124"
        "\1\125\1\60\1\132\1\111\1\106\1\114\1\102\2\60\1\124\1\uffff\1\111"
        "\1\117\1\131\1\117\1\114\2\uffff\1\60\1\106\1\116\1\60\1\103\1\117"
        "\1\uffff\1\131\1\137\1\uffff\1\113\1\103\1\60\1\102\1\60\1\113\1"
        "\uffff\1\114\1\uffff\1\60\1\117\1\uffff\1\103\1\113\1\60\1\uffff"
        )

    DFA18_max = DFA.unpack(
        "\1\172\1\52\2\uffff\1\71\1\uffff\2\71\4\uffff\1\116\1\105\1\116"
        "\1\125\1\123\1\105\1\117\1\122\1\125\1\110\1\101\1\111\1\124\1\uffff"
        "\1\145\4\uffff\1\71\4\uffff\1\124\1\104\1\106\1\104\1\132\2\172"
        "\1\124\1\172\1\124\1\172\1\116\1\124\1\114\1\122\1\105\1\122\1\124"
        "\4\uffff\1\71\1\uffff\1\125\2\172\1\125\1\137\1\103\1\132\2\uffff"
        "\1\110\1\uffff\1\172\1\uffff\1\107\1\114\1\101\1\105\1\115\1\116"
        "\1\137\1\110\1\145\1\172\2\uffff\1\125\1\132\1\126\1\124\1\111\1"
        "\117\1\uffff\1\105\1\172\1\111\3\172\1\117\1\172\1\uffff\1\114\1"
        "\132\1\105\2\125\1\101\1\111\1\106\1\104\1\172\1\uffff\1\116\1\114"
        "\3\uffff\1\116\1\125\1\uffff\1\124\1\111\1\106\1\132\1\114\1\122"
        "\1\117\1\131\1\172\1\uffff\1\172\1\117\1\120\1\124\1\172\1\106\1"
        "\125\1\103\1\132\1\105\1\172\1\116\1\172\2\uffff\1\103\1\125\1\120"
        "\1\uffff\1\131\1\132\1\124\1\111\1\102\1\uffff\1\137\1\uffff\1\113"
        "\1\124\1\125\1\172\1\132\1\111\1\106\1\114\1\102\2\172\1\124\1\uffff"
        "\1\111\1\117\1\131\1\117\1\114\2\uffff\1\172\1\106\1\116\1\172\1"
        "\103\1\117\1\uffff\1\131\1\137\1\uffff\1\113\1\103\1\172\1\102\1"
        "\172\1\113\1\uffff\1\114\1\uffff\1\172\1\117\1\uffff\1\103\1\113"
        "\1\172\1\uffff"
        )

    DFA18_accept = DFA.unpack(
        "\2\uffff\1\2\1\3\1\uffff\1\5\2\uffff\1\11\1\12\1\13\1\14\15\uffff"
        "\1\54\1\uffff\1\61\1\60\1\1\1\4\1\uffff\1\6\1\10\1\7\1\57\22\uffff"
        "\1\51\1\52\1\53\1\56\1\uffff\1\55\7\uffff\1\31\1\32\1\uffff\1\34"
        "\1\uffff\1\36\12\uffff\1\16\1\17\6\uffff\1\35\10\uffff\1\15\12\uffff"
        "\1\40\2\uffff\1\42\1\44\1\45\2\uffff\1\50\11\uffff\1\37\15\uffff"
        "\1\33\1\41\3\uffff\1\20\5\uffff\1\26\1\uffff\1\30\14\uffff\1\21"
        "\5\uffff\1\43\1\46\6\uffff\1\47\2\uffff\1\24\6\uffff\1\22\1\uffff"
        "\1\25\2\uffff\1\27\3\uffff\1\23"
        )

    DFA18_special = DFA.unpack(
        "\u00cb\uffff"
        )


    DFA18_transition = [
        DFA.unpack("\2\33\2\uffff\1\33\22\uffff\1\33\7\uffff\1\1\1\2\1\3"
        "\1\4\1\5\1\6\1\7\1\10\12\32\1\11\1\12\1\uffff\1\13\3\uffff\1\14"
        "\2\31\1\15\1\16\1\17\2\31\1\20\3\31\1\21\1\22\1\23\2\31\1\24\1\31"
        "\1\25\1\31\1\26\1\27\3\31\4\uffff\1\30\1\uffff\32\31"),
        DFA.unpack("\1\34"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\12\37"),
        DFA.unpack(""),
        DFA.unpack("\12\37"),
        DFA.unpack("\1\41\1\uffff\12\43"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\44\12\uffff\1\45"),
        DFA.unpack("\1\46"),
        DFA.unpack("\1\47"),
        DFA.unpack("\1\50"),
        DFA.unpack("\1\51\14\uffff\1\52"),
        DFA.unpack("\1\53"),
        DFA.unpack("\1\54\13\uffff\1\55"),
        DFA.unpack("\1\56"),
        DFA.unpack("\1\57\3\uffff\1\60\17\uffff\1\61"),
        DFA.unpack("\1\62\2\uffff\1\63"),
        DFA.unpack("\1\64"),
        DFA.unpack("\1\65"),
        DFA.unpack("\1\66\5\uffff\1\67\1\70"),
        DFA.unpack(""),
        DFA.unpack("\1\72\1\uffff\12\32\13\uffff\1\43\37\uffff\1\43"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\73\1\uffff\12\37"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\74\20\uffff\1\75"),
        DFA.unpack("\1\76"),
        DFA.unpack("\1\77"),
        DFA.unpack("\1\100"),
        DFA.unpack("\1\101\13\uffff\1\102"),
        DFA.unpack("\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack("\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack("\1\105"),
        DFA.unpack("\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack("\1\107"),
        DFA.unpack("\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack("\1\111"),
        DFA.unpack("\1\112\22\uffff\1\113"),
        DFA.unpack("\1\114"),
        DFA.unpack("\1\115"),
        DFA.unpack("\1\116"),
        DFA.unpack("\1\117"),
        DFA.unpack("\1\120"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\12\121"),
        DFA.unpack(""),
        DFA.unpack("\1\122"),
        DFA.unpack("\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack("\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack("\1\125\23\uffff\1\126"),
        DFA.unpack("\1\127"),
        DFA.unpack("\1\130"),
        DFA.unpack("\1\131"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\132"),
        DFA.unpack(""),
        DFA.unpack("\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack(""),
        DFA.unpack("\1\134"),
        DFA.unpack("\1\135"),
        DFA.unpack("\1\136"),
        DFA.unpack("\1\137"),
        DFA.unpack("\1\140"),
        DFA.unpack("\1\141"),
        DFA.unpack("\1\142"),
        DFA.unpack("\1\143"),
        DFA.unpack("\12\121\13\uffff\1\43\37\uffff\1\43"),
        DFA.unpack("\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\145"),
        DFA.unpack("\1\146"),
        DFA.unpack("\1\147\1\uffff\1\150\13\uffff\1\151\3\uffff\1\152"),
        DFA.unpack("\1\153"),
        DFA.unpack("\1\154"),
        DFA.unpack("\1\155"),
        DFA.unpack(""),
        DFA.unpack("\1\156"),
        DFA.unpack("\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack("\1\160"),
        DFA.unpack("\12\31\7\uffff\1\31\1\161\30\31\4\uffff\1\31\1\uffff"
        "\32\31"),
        DFA.unpack("\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack("\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack("\1\165\5\uffff\1\166"),
        DFA.unpack("\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack(""),
        DFA.unpack("\1\170"),
        DFA.unpack("\1\171"),
        DFA.unpack("\1\172"),
        DFA.unpack("\1\173"),
        DFA.unpack("\1\174"),
        DFA.unpack("\1\175"),
        DFA.unpack("\1\176"),
        DFA.unpack("\1\177"),
        DFA.unpack("\1\u0080"),
        DFA.unpack("\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack(""),
        DFA.unpack("\1\u0082"),
        DFA.unpack("\1\u0083"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u0084"),
        DFA.unpack("\1\u0085"),
        DFA.unpack(""),
        DFA.unpack("\1\u0086"),
        DFA.unpack("\1\u0087"),
        DFA.unpack("\1\u0088"),
        DFA.unpack("\1\u0089\13\uffff\1\u008a"),
        DFA.unpack("\1\u008b"),
        DFA.unpack("\1\u008c"),
        DFA.unpack("\1\u008d"),
        DFA.unpack("\1\u008e"),
        DFA.unpack("\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack(""),
        DFA.unpack("\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack("\1\u0091"),
        DFA.unpack("\1\u0092"),
        DFA.unpack("\1\u0093"),
        DFA.unpack("\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack("\1\u0095"),
        DFA.unpack("\1\u0096"),
        DFA.unpack("\1\u0097"),
        DFA.unpack("\1\u0098"),
        DFA.unpack("\1\u0099"),
        DFA.unpack("\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack("\1\u009b"),
        DFA.unpack("\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\1\u009d"),
        DFA.unpack("\1\u009e"),
        DFA.unpack("\1\u009f"),
        DFA.unpack(""),
        DFA.unpack("\1\u00a0"),
        DFA.unpack("\1\u00a1"),
        DFA.unpack("\1\u00a2"),
        DFA.unpack("\1\u00a3"),
        DFA.unpack("\1\u00a4"),
        DFA.unpack(""),
        DFA.unpack("\1\u00a5"),
        DFA.unpack(""),
        DFA.unpack("\1\u00a6"),
        DFA.unpack("\1\u00a7"),
        DFA.unpack("\1\u00a8"),
        DFA.unpack("\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack("\1\u00aa"),
        DFA.unpack("\1\u00ab"),
        DFA.unpack("\1\u00ac"),
        DFA.unpack("\1\u00ad"),
        DFA.unpack("\1\u00ae"),
        DFA.unpack("\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack("\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack("\1\u00b1"),
        DFA.unpack(""),
        DFA.unpack("\1\u00b2"),
        DFA.unpack("\1\u00b3"),
        DFA.unpack("\1\u00b4"),
        DFA.unpack("\1\u00b5"),
        DFA.unpack("\1\u00b6"),
        DFA.unpack(""),
        DFA.unpack(""),
        DFA.unpack("\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack("\1\u00b8"),
        DFA.unpack("\1\u00b9"),
        DFA.unpack("\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack("\1\u00bb"),
        DFA.unpack("\1\u00bc"),
        DFA.unpack(""),
        DFA.unpack("\1\u00bd"),
        DFA.unpack("\1\u00be"),
        DFA.unpack(""),
        DFA.unpack("\1\u00bf"),
        DFA.unpack("\1\u00c0"),
        DFA.unpack("\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack("\1\u00c2"),
        DFA.unpack("\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack("\1\u00c4"),
        DFA.unpack(""),
        DFA.unpack("\1\u00c5"),
        DFA.unpack(""),
        DFA.unpack("\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack("\1\u00c7"),
        DFA.unpack(""),
        DFA.unpack("\1\u00c8"),
        DFA.unpack("\1\u00c9"),
        DFA.unpack("\12\31\7\uffff\32\31\4\uffff\1\31\1\uffff\32\31"),
        DFA.unpack("")
    ]

    # class definition for DFA #18

    class DFA18(DFA):
        pass


 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(FCLLexer)

    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)



if __name__ == '__main__':
    main(sys.argv)
