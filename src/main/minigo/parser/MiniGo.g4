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

declarations: declare declareTail ;

declare:
    constDeclare
|   varDeclare
|   typeDeclare
|   funcDeclare
;

declareTail: NL* declare declareTail | ;

constDeclare: CONST ID ASSIGN expr SEMICOLON ;

varDeclare: VAR ID (arrayType|varType)? init? SEMICOLON ;

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

method: ID LB parameters? RB (varType|arrayType)? ;

parameters: ID (varType|arrayType)? paraTail ;

paraTail: COMMA parameters paraTail | ;

funcDeclare: FUNC methodDeclare? method LC NL* (stmt NL*)* RC NL ;

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
|    returnstmt) (SEMICOLON NL|SEMICOLON|NL) ;

assignment: lhs assignOp (expr|arrayInit) ;

lhs:
    ID
|   arrayElement
|   structField
;

assignOp:
    COLON ASSIGN
|   ADDASS
|   SUBASS
|   MULASS
|   DIVASS
|   MODASS
;

ifstmt: IF LB expr RB LC NL* stmt* RC elsestmt? ;

elsestmt:
    ELSE (ifstmt | LC NL* stmt* RC) ;

forstmt:
    FOR (expr
    |    initFor
    |    rangeFor) LC NL* stmt* RC ;

initFor:
    (assignment
|    VAR ID (varType|arrayType)? init) SEMICOLON expr SEMICOLON assignment ;

rangeFor: ('index'|'_') COMMA ('value'|'_') COLON ASSIGN RANGE (ID|arrayLit) ;

breakstmt: BREAK ;

contstmt: CONTINUE ;

returnstmt: RETURN expr? ;

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
    expr2 (EQ|UNEQ|LESS|LESSEQ|GREATER|GREATEREQ) expr3
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
    <assoc=right> (NOT|SUBTR) expr6
|   expr6
;

expr6:
    arrayElement
|   structField
|   expr7
;

arrayElement: ID index+ ;

index: LP expr RP ;

structField: ID '.' ID ;

expr7:
    funcCall
|   methodCall
|   expr8
;

funcCall: ID LB arguments? RB ;

arguments: expr argTail ;

argTail: COMMA expr argTail | ;

methodCall: ID '.' funcCall ;

expr8:
    LB expr RB
|   literal
;

arrayInit: arrayType arrayLit? ;

literal:
    INTLIT
|   FLOATLIT
|   BOOLLIT
|   STRINGLIT
|   arrayLit
|   structLit
|   ID
;

arrayLit: LC literal literalTail RC literalTail ;

literalTail: COMMA literal literalTail | ;

structLit: ID LC structElement? RC ;

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
GREATER: '>' ;
GREATEREQ: '>=' ;
AND: '&&' ;
OR: '||' ;
NOT: '!' ;
ASSIGN: '=' ;
ADDASS: '+=' ;
SUBASS: '-=' ;
MULASS: '*=' ;
DIVASS: '/=' ;
MODASS: '%=' ;

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

HEXADECIMAL: '0' ('x'|'X') [0-9a-fA-F]+ { self.text = str(int(self.text, 16)) };

INTLIT:
    DECIMAL
|   BINARY
|   OCTAL
|   HEXADECIMAL
;

FLOATLIT:
    ([0-9]|[1-9] [0-9]*) '.' [0-9]*
|   ([0-9]|[1-9] [0-9]*) '.' [0-9]* ('e'|'E') ('+'|'-')? [0-9]+
;

DECIMAL:
    [0-9]
|   [1-9] [0-9]+
;

BINARY: '0' ('b'|'B') ('1'|'0')+ ;

OCTAL: '0' ('o'|'O') [0-7]+ ;

BOOLLIT: TRUE | FALSE ;

TRUE: 'true' ;
FALSE: 'false' ;

STRINGLIT: '"' ('\\' [ntr"\\] | ~["\\\r\n])* '"' {
    self.text = self.text[1:-1]
};

// Comment

fragment COMMENT_CONTENT: ( ~[*] | '*' ~[/] | COMMENT )*;

COMMENT: (('//' ~[\r\n]* [\r\n]+) | ('/*' COMMENT_CONTENT '*/')) -> skip ;

// White spaces

WS : [ \t\b\f]+ -> skip ; // skip spaces, tabs

ERROR_CHAR: . {raise ErrorToken(self.text)} ;
ILLEGAL_ESCAPE: '"' ('\\' [ntr"\\] | ~["\\])* ('\\' ~[tnr"\\] | '\\') { raise IllegalEscape(self.text[1:]) };
UNCLOSE_STRING: '"' ([#-~ !]| [\r\n\b\f\t] | ('\'' '"'))* [\r\n]+ {
    self.text = self.text[1:]
    self.text = self.text.replace('\n','')
    self.text = self.text.replace('\r','')
    raise UncloseString(self.text)
};
