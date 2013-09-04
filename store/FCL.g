grammar FCL;

options
{
   language = Python3;
}

@lexer::header
{
#!/usr/bin/python3
}

@header
{
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

}

@init
{
self.system = None
self.scope = {}
}


function_block_type
	:	'_MAMDAMI_' | '_SUGENO_' | '_TSUKAMOTO_'
	;
function_block_declaration
	:	'FUNCTION_BLOCK' function_block_type? name=IDENTIFIER
		{self.system = get_system($name.text, $function_block_type.text)}
		{self.type_ = $function_block_type.text}
		fb_io_var_declarations*
		//other_var_declarations*
        function_block_body
	    'END_FUNCTION_BLOCK'
	    //{for item in self.scope.items(): print(item)}
        EOF
    ;
    
	
fb_io_var_declarations
	:	input_declarations|
		output_declarations
	;
	
input_declarations
	:	'VAR_INPUT'
		variable_declaration+
		'END_VAR'
	;
	
output_declarations
	:	'VAR_OUTPUT' 'RETAIN'?
		variable_declaration+
		'END_VAR'
	;
	
variable_declaration
	:
		name=IDENTIFIER ':' type ';'
		{self.scope[$name.text] = Variable($name.text)}
	;

/*
other_var_declarations
	:	var_declarations*
	;

var_declarations
	:	'VAR' ('CONSTANT'?)
		variable_declaration+
	;
*/

//only support for REAL type
type	:	'REAL' | IDENTIFIER ; //'BOOL';

/*output_declaration
	:	IDENTIFIER ':' type ';'
	;

other_var_declarations
	:	var_declarations
	;
*/

function_block_body
	:	fuzzify_block*
		defuzzify_block*
		(rb=rule_block {self.system.add_blocks(rb)} )*
		//option_block*
	;

rule_block returns[ruleblock]
	:	'RULEBLOCK' name=IDENTIFIER
		operator=operator_definition
		activation=activation_method?
		accumulation=accumulation_method
		{ruleblock = RuleBlock(name.text, operator, activation, accumulation)}
		{tnorm = ruleblock.and_}
		{snorm = ruleblock.or_}
		{cnorm = ruleblock.not_}
		(r=rule[tnorm, snorm, cnorm] {ruleblock.addrule(r)}) *
		'END_RULEBLOCK'
	;

operator_definition returns[operators]
	:	((('OR' ':' or_=IDENTIFIER ';') ('AND' ':' and_=IDENTIFIER ';')?) |
		(('AND' ':' and_=IDENTIFIER ';') ('OR' ':' or_=IDENTIFIER ';')?))
		('NOT' ':' not_ = IDENTIFIER ';')?
		//{$operator = ($and_.text if and_ else None, $or_.text if or_ else None)}
		{$operators = (and_ and $and_.text, or_ and $or_.text, not_ and $not_.text)}
		{$operators = check_op($operators)}
		
		//(('OR' ':' op=('MAX' | 'ASUM' | 'BSUM'))|
		//('AND' ':' op=('MIN' | 'PROD' | 'BDIF'))) ';'
		//{$operator = $op.text}
	;
		
//complement_operator returns[operator]
//	:	('NOT' ':' op=(IDENTIFIER))
//		{$operator = $op.text}
//	;

activation_method returns[activation]
	:	'ACT' ':' act=IDENTIFIER ';' //('PROD' | 'MIN') ';'
		{$activation = $act.text}
	;

accumulation_method returns[accumulation]
	:	'ACCU' ':' accu=IDENTIFIER ';' //('MAX' | 'BSUM' | 'NSUM') ';'
		{$accumulation = $accu.text}
	;

rule[tnorm, snorm, cnorm] returns[rule_]
	:	'RULE' INTEGRAL_LITERAL ':'
		'IF' c1=condition[tnorm, snorm, cnorm] 'THEN' c2=conclusion ('WITH' w=weighting_factor)? ';'
		{rule_ = Rule.get_rule(c1, c2, w or 1)}
	;

condition[tnorm, snorm, cnorm] returns[operator_tree]
	:	res=expr[tnorm, snorm, cnorm] {operator_tree = res}
	;

expr[tnorm, snorm, cnorm] returns[res]
	:	t = term[tnorm, snorm, cnorm]
		('OR' e = expr[tnorm, snorm, cnorm])?
		{res = Or(t, e, snorm) if e is not None else t}
	;

/*expr_[tnorm, snorm] returns[e]
@init{
e = None
}
	:	('OR' e = expr[tnorm, snorm])?
	;*/

term[tnorm, snorm, cnorm] returns[t]
	:	( e=pred[cnorm] | n='NOT'? '(' e=expr[tnorm, snorm, cnorm] ')' )
		('AND't_ = term[tnorm, snorm, cnorm])?
		{t = e if n is None else Not(e, cnorm)}
		{t = t if t_ is None else And(t,t_, tnorm)}
	;

/*term_[tnorm, snorm] returns[t]
	:
	;*/

pred[cnorm] returns[res]
	:	var=IDENTIFIER 'IS' (n='NOT')? t=IDENTIFIER {p = Predicate(self.scope[var.text], self.scope[var.text + t.text])}
		{res = p if n is None else Not(p, cnorm)}
	;
	


/*condition
	:	s=subcondition (('AND' | 'OR') subcondition)* //| '(' condition ')'
	;
*/

/*subcondition returns[res]
	:	('NOT' '(' var=variable_name (('IS' not_='NOT'?)| '.') t=term_name ')')
		{res = Predicate(self.scope[var.text], self.scope[var.text + t.text])}
		{res = res if not_ is not None else Not(res)}
		|
		//('NOT' '(' cond=condition ')') |
		( var=variable_name (('IS' not_='NOT'?)| '.') t=term_name )
		{res = Predicate(self.scope[var.text], self.scope[var.text + t.text])}
		{res = res if not_ is None else Not(res)}
	;
*/

conclusion returns[res]
	:	//mc = mconclusion {res = mc} |
		//sc = sconclusion {res = sc}
		c = (mconclusion | sconclusion)
		{res = c}
	;

mconclusion returns[res]
@init{
res = []
}
@after{
if self.type_ == '_TSUKAMOTO_':
	res = res[0]
}
	:	var=IDENTIFIER ('IS' | '.') t=IDENTIFIER {res.append(Predicate(self.scope[var.text], self.scope[var.text + t.text]))}
		(',' var_=IDENTIFIER ('IS' | '.') t_=IDENTIFIER {res.append(Predicate(self.scope[var_.text], self.scope[var_.text + t_.text]))} )*
	;
	
sconclusion returns[res]
	:	(i=IDENTIFIER | n=numeric_literal) (o=('+'|'-'|'*''*'?|'/''/'?) sc=sconclusion )?
		{s = $i.text if i is not None else $n.text}
		{res = s + $o.text + sc if sc is not None else s}
	;

tconclusion returns[res]
@init{
res = None
}
	:	var=IDENTIFIER ('IS' | '.') t=IDENTIFIER {res = Predicate(self.scope[var.text], self.scope[var.text + t.text])}
	;

weighting_factor returns[value]
	:	name=IDENTIFIER {value = scope[name.text]} |
		n=numeric_literal {value = float($n.text)}
	;

fuzzify_block
	:	'FUZZIFY' name=IDENTIFIER
		{variable = self.scope[$name.text]}
		(adjective=linguistic_term[variable])* //{variable.adjectives.append(adjective)}
		'END_FUZZIFY'
	;

defuzzify_block
	:	'DEFUZZIFY' name=IDENTIFIER {variable = self.scope[$name.text]}
		(adjective=linguistic_term[variable])* //[$name]* //{variable.adjectives.append(adjective)}
		defuzzification=defuzzification_method
		{variable.defuzzification = defuzzification}
		default=default_value
		{variable.default = default}
		r=range?
		'END_DEFUZZIFY'
	;

variable_name	:	IDENTIFIER	;

linguistic_term[variable] returns[adjective]
	:	'TERM' name=IDENTIFIER	':''=' fset=membership_function ';'
		{adjective = Adjective(name.text, fset)}
		{variable.adjectives.append(adjective)}
		{self.scope[variable.name + name.text]=adjective}
	;

term_name	:	IDENTIFIER	;

membership_function returns[fuzzy_set]
	:	fset = ( singleton | points | other_function)
		{fuzzy_set = fset}
	;

singleton returns[fset]
	:	(n=numeric_literal {fset = get_fset('Singleton', [float($n.text)])}) //{fset=singleton.Singleton(float($n.text))}
		|
		(v=variable_name {fset = get_fset('Singleton', self.scope[$v.text]) }) //{fset=singleton.Singleton(self.scope[$v.text])}
	;

points	returns[fset]
@init{
points=[]
}
	:	('(' (x=numeric_literal|variable_name) ',' y=numeric_literal ')' {points.append((float($x.text), float($y.text)))} ) *
		//{fset = polygon.Polygon(*points)}
		{fset = get_fset('Polygon', points)}
	;


defuzzification_method returns[method]
	:	'METHOD' ':' m=IDENTIFIER ';' //('COG' | 'COGS' | 'COA' | 'LM' | 'RM') ';'
		{method = $m.text}
	;
other_function returns[fset]
@init{
params = []
}
	:	name=IDENTIFIER
		'('
		(p = function_param {params.append(p)}
		(',' p_=function_param {params.append(p_)})*
		)?
		')'
		{fset = get_fset($name.text, params)}
	;

function_param returns[param]
	:	 p=numeric_literal {param = float($p.text)} |
		( '(' x=numeric_literal ',' y=numeric_literal ')'
		{param = (float($x.text), float($y.text))})
	;


default_value returns[value]
@init{
value = None
}
	:	'DEFAULT' ':''='
		(num=numeric_literal {value=float($num.text)}
		|
		'NC')
		';'
	;

range returns[interval]
	:	'RANGE' ':''=' '(' x=numeric_literal '..' y=numeric_literal ')' ';'
		{interval = Interval(float($x.text), float($y.text))}
	;

/*numeric_literal returns[value]
	:	i=INTEGRAL_LITERAL {value = int(i.text)}|
		r=REAL_LITERAL {value = float(r.text)}{print(r, r.text)}
	;
*/
numeric_literal
	:	INTEGRAL_LITERAL|
		REAL_LITERAL
	;


/* --- LEXER RULES --- */

//IDENTIFIER  :	(('a'..'z'|'A'..'Z')|('_'('a'..'z'|'A'..'Z'|'0'..'9'))) ('a'..'z'|'A'..'Z'|'0'..'9'|'_')*    ;
//IDENTIFIER  :	('a'..'z'|'A'..'Z'|'_') ('a'..'z'|'A'..'Z'|'0'..'9'|'_')*    ;
IDENTIFIER  :	LETTER (LETTER_ | DIGIT)*    ;

fragment LETTER	:	'a'..'z'|'A'..'Z';
fragment LETTER_	:	'a'..'z'|'A'..'Z'|'_';

REAL_LITERAL	:	('+'|'-')? DIGIT+  '.' DIGIT+	;
	
INTEGRAL_LITERAL	:	('+'|'-')? ('0'..'9')+	;
fragment DIGIT :	'0'..'9'+    ;

FLOAT
    :   ('0'..'9')+ '.' ('0'..'9')* EXPONENT?
    |   '.' ('0'..'9')+ EXPONENT?
    |   ('0'..'9')+ EXPONENT
    ;

COMMENT    :   '(*' ( options {greedy=false;} : . )* '*)' {$channel=HIDDEN;}    ;

WS  :   ( ' '
        | '\t'
        | '\r'
        | '\n'
        ) {$channel=HIDDEN;}
    ;

fragment
EXPONENT : ('e'|'E') ('+'|'-')? ('0'..'9')+ ;

