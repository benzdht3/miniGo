grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text);
    else:
        return super().emit();
}

options{
	language=Python3;
}

// PARSER

program: NL* declarations NL* EOF ;

// DECLARATION

declarations:
    constDeclare
|   varDeclare
|   typeDeclare
|   funcDeclare
;

constDeclare: CONST ID ASSIGN value SEMICOLON ;

value:
    literals
|   expr
;

varDeclare: VAR ID (varType|arrayType)? init? SEMICOLON ;

varType:
    INT
|   FLOAT
|   STRING
|   BOOLEAN
;

arrayType: dimensions+ (varType|STRUCT) ;

dimensions: LP (INTLIT|ID) RP;

init: ASSIGN expr ;

typeDeclare: TYPE ID (structDeclare|interfaceDeclare) ;

structDeclare: STRUCT LC (field)* RC (NL|SEMICOLON) ;

field: NL* ID (varType
            |  structDeclare
            |  arrayType
            |  interfaceDeclare) (SEMICOLON|NL) ;

interfaceDeclare: INTERFACE LC method* RC (SEMICOLON|NL);

method: ID LB parameters? RB (varType|arrayType) ;

parameters: ID (varType|arrayType)? paraTail ;

paraTail: COMMA parameters paraTail | ;

funcDeclare: FUNC methodDeclare? method LC stmt+ RC NL ;

methodDeclare: LB ID ID RB ;

// STATEMENTS

stmt:
    (varDeclare
|    constDeclare
|    assignment
|    ifstmt
|    forstmt
|    breakstmt
|    contstmt
|    funcCall
|    methodCall
|    returnstmt) (SEMICOLON|NL) ;

assignment: lhs assignOp expr ;

lhs:
    ID
|   arrayElement
|   structField

assignOp:
    COLON EQUAL
|   ADDASS
|   SUBASS
|   MULASS
|   DIVASS
|   MODASS
;

ifstmt: IF LB expr RB LC NL* stmt* RC elsestmt?

elsestmt:
    ifstmt
|   LC NL* stmt* RC
;

forstmt:
    (expr
|    three
|    range) LC NL* stmt* RC ;
;

three:
    (assignment
|    VAR ID (varType|arrayType)? init) SEMICOLON expr SEMICOLON assignment ;

range: ('index'|'_') COMMA ('value'|'_') DOT EQUAL RANGE (ID|arrayLit) ;

breakstmt: BREAK SEMICOLON ;

contstmt: CONTINUE SEMICOLON ;

returnstmt: RETURN expr? SEMICOLON ;

// EXPRESSION

expr:
    expr OR expr1
|   expr1
;

expr1:
    expr1 AND expr2
|   expr2
;

expr2:
    expr2 (EQ|UNEQ|LESS|LESSEQ|MORE|MOREEQ) expr3
|   expr3
;

expr3:
    expr3 (ADD|SUBTR) expr4
|   expr4
;

expr4:
    expr4 (MUL|DIV|MOD) expr5
|   expr5
;

expr5:
    <assoc=right> (NOTOP|SUBTR) expr6
|   expr6
;

expr6:
    arrayElement
|   structField
|   expr7
;

arrayElement: ID index+ ;

index: LP expr RP ;

structField: ID DOT ID ;

expr7:
    funcCall
|   methodCall
|   expr8
;

funcCall: ID LB arguments? RB ;

arguments: expr argTail ;

argTail: COMMA expr argTail | ;

methodCall: ID DOT funcCall ;

expr8:
    LB expr RB
|   operands
;

operands:
    ID
|   literals
;

literal:
    INTLIT
|   FLOATLIT
|   BOOLLIT
|   STRINGLIT
|   arrayLit
|   structLit
;

arrayLit: arrayType literals? ;

literals:
    LC literal literalTail RC
|   literal literalTail
;

literalTail: COMMA (literal literalTail | LC literal literalTail RC) | ;

structLit: ID LC structElements? RC ;

structElement: ID COLON expr elementTail;

elementTail: COMMA structElement | ;

// LEXICAL

// Seperators

LB: '(' ;
RB: ')' ;
LC: '{' ;
RC: '}' ;
LP: '[' ;
RP: ']' ;
COMMA: ',' ;
SEMICOLON: ';' ;
COLON: ':' ;

// Operators

ADD: '+' ;
SUBTR: '-' ;
MUL: '*' ;
DIV: '/' ;
MOD: '%' ;
EQ: '==' ;
UNEQ: '!=' ;
LESS: '<' ;
LESSEQ: '<=' ;
MORE: '>' ;
MOREEQ: '>=' ;
AND: '&&' ;
OR: '||' ;
NOT: '!' ;
ASSIGN: '=' ;
ADDASS: '+=' ;
SUBASS: '-=' ;
MULASS: '*=' ;
DIVASS: '/=' ;
MODASS: '%=' ;
DOT: '.' ;

// Keywords

IF: 'if' ;
ELSE: 'else' ;
FOR: 'for' ;
RETURN: 'return' ;
FUNC: 'func' ;
TYPE: 'type' ;
STRUCT: 'struct' ;
INTERFACE: 'interface' ;
STRING: 'string' ;
INT: 'int' ;
FLOAT: 'float' ;
BOOLEAN: 'boolean' ;
CONST: 'const' ;
VAR: 'var' ;
CONTINUE: 'continue' ;
BREAK: 'break' ;
RANGE: 'range' ;
NIL: 'nil' ;

// Identifier

ID: [a-zA-Z_] [a-zA-Z_0-9]* ;

// Newline

NL:
    '\n'
|   '\r\n'
|   '\r'
;

// Literals

INTLIT:
    DECIMAL
|   BINARY
|   OCTAL
|   HEXADECIMAL
;

DECIMAL:
    [0-9]
|   [1-9] [0-9]+
;

BINARY: 0 (b|B) (1|0)+ ;

OCTAL: 0 (o|O) [0-7]+ ;

HEXADECIMAL: 0 (x|X) [0-9a-fA-F]+ ;

FLOATLIT:
    [0-9] '.' [0-9]*
|   [0-9] '.' [0-9] (e|E) (+|-)? [0-9]+
;

BOOLLIT: TRUE | FALSE ;

TRUE: 'true' ;
FALSE: 'false' ;

STRINGLIT: '"' (~[\r\n"] | [\b\f\t'\\] | ('\'' '"'))* '"' {
			txt = self.text[1:-1]
			pos = 0
			l = len(txt)
			while pos < l:
				while pos < l and txt[pos] != '\\':
					pos += 1
				pos += 1
				if pos < l:
					escap = txt[pos]
					if escap != 't' and escap != 'r' and escap != '\"' and escap != 'n' and escap != '\\':
						raise IllegalEscape(txt[:pos+1])
					else:
						pos += 1
				else:
					self.text=txt
			self.text=txt
		};

// Comment

COMMENT: (('//' (~[\n])*) | ('/*' .* '*/')) -> skip ;

// White spaces

WS : [ \t\b\f]+ -> skip ; // skip spaces, tabs

ERROR_CHAR: . {raise ErrorToken(self.text)} ;
ILLEGAL_ESCAPE: . {raise IllegalEscape(self.text)} ;
UNCLOSE_STRING: '"' ([#-~ !]| [\b\f\t] | ('\'' '"'))* {raise UncloseString(self.text[1:])} ;
