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

// Seperators

LB: '(' ;
RB: ')' ;
LC: '{' ;
RC: '}' ;
LP: '[' ;
RP: ']' ;
COMMA: ',' ;
SEMICOLON: ';' ;


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
CONCAT: '.' ;

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

INTEGER:
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

FLOAT:
    [0-9] '.' [0-9]*
|   [0-9] '.' [0-9] (e|E) (+|-)? [0-9]+
;

BOOLEAN: TRUE | FALSE ;

TRUE: 'true' ;
FALSE: 'false' ;

STRING: '"' (~[\r\n"] | [\b\f\t'\\] | ('\'' '"'))* '"' {
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
