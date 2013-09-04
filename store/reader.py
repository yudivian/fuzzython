#!/usr/bin/python3

from .FCLLexer import FCLLexer
from .FCLParser import FCLParser
import antlr3

__author__ = ''

#
# error in antlr-3.5 lexer ... change AL method by AT
#

def load_from_file(filename):
    """
    Parse a FCL file to a fuzzy.systems (Mamdani, Sugeno or Tsukamoto) instance
    """
    return __load(antlr3.ANTLRFileStream(filename))

def load_from_string(string):
    """
    Parse a FCL string to a fuzzy.systems (Mamdani, Sugeno or Tsukamoto) instance
    """
    return __load(antlr3.ANTLRStringStream(string))

def __load(input_):
    """
    Parse a FCL input to a fuzzy.systems (Mamdani, Sugeno or Tsukamoto) instance
    """
    try:
        lexer = FCLLexer(input_)
        tokens = antlr3.CommonTokenStream(lexer)
        parser = FCLParser(tokens)
        parser.function_block_declaration()
        return parser.system
    except Exception as e:
        print('--- incorrect FCL-E file ---')
        print(e)
        #raise e
        return None

__all__ = ['load_from_string', 'load_from_file']



