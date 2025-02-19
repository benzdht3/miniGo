grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
def __init__(self, input=None, output:TextIO = sys.stdout):
    super().__init__(input, output)
    self.checkVersion("4.9.2")
    self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
    self._actions = None
    self._predicates = None
    self.preType = None

def emit(self):
    tk = self.type
    self.preType = tk;
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

declareTail: NL* declare NL* declareTail | ;

constDeclare: CONST identifier init endStmt ;
varDeclare: VAR identifier modify endStmt ;

modify: (arrayType | varType | identifier) | init | ((arrayType | varType | identifier) init) ;

varType: INT | FLOAT | STRING | BOOLEAN ;

arrayType: dimensions+ (varType | STRUCT | identifier) ;

dimensions: LP (INTLIT | identifier) RP ;

init: INITOP (expr | arrayInit) ;

typeDeclare: TYPE identifier (structDeclare | interfaceDeclare) ;

structDeclare: STRUCT LC field+ RC endStmt ;

field: identifier (varType | structDeclare | arrayType | interfaceDeclare | identifier) endStmt ;

interfaceDeclare: INTERFACE LC NL* method+ endStmt+ RC endStmt ;

method: identifier LB (parameters paraTail)? RB (varType | arrayType | identifier)? endStmt* ;

parameters: identifier (COMMA identifier)* (varType | arrayType | identifier) ;
paraTail: COMMA parameters paraTail | ;

funcDeclare: FUNC methodDeclare? method LC NL* stmt* RC endStmt ;

methodDeclare: LB identifier identifier RB ;

// STATEMENTS

stmt: (varDeclare | constDeclare) | (statement endStmt) ;

statement:
    assignment
  | ifstmt
  | forstmt
  | breakstmt
  | contstmt
  | funcCall
  | methodCall
  | returnstmt ;

assignment: lhs assignOp+ (expr | arrayInit) ;

lhs: identifier index*
   | (identifier | identifier index+) (DOT identifier index*)+ ;

assignOp: ASSIGN | ADDASS | SUBASS | MULASS | DIVASS | MODASS ;

ifstmt: IF LB expr RB NL* LC NL* stmt* RC elsestmt? ;

elsestmt: ELSE (ifstmt | NL* LC NL* stmt* RC NL*) ;

forstmt: FOR (expr | initFor | rangeFor) LC NL* stmt* RC ;

initFor: (assignment_for | (VAR identifier (varType | arrayType)? init)) endStmt expr endStmt assignment_for ;

assignment_for: ID assignOp literal ;

rangeFor: ('index' | '_') COMMA ('value' | '_') ASSIGN RANGE (identifier | literal | arrayElement) ;

breakstmt: BREAK ;
contstmt: CONTINUE ;
returnstmt: RETURN expr? ;

// EXPRESSION

expr: expr OR expr1 | expr1 ;
expr1: expr1 AND expr2 | expr2 ;
expr2: expr2 (EQ | UNEQ | LESS | LESSEQ | GREATER | GREATEREQ) expr3 | expr3 ;
expr3: expr3 (ADD | SUBTR) expr4 | expr4 ;
expr4: expr4 (MUL | DIV | MOD) expr5 | expr5 ;
expr5: <assoc=right> (NOT | SUBTR)* expr6 | expr6 ;
expr6: arrayElement | methodCallExpr | expr7 ;

arrayElement: (expr8 | funcCall) index+ ;
index: LP expr RP ;
structField: (identifier | arrayElement | structLit) (DOT ( identifier | funcCall) index*)+ ;
expr7: structField | funcCall | expr8 ;

funcCall: identifier LB arguments? RB ;

arguments: expr argTail ;
argTail: COMMA expr argTail | ;

methodCallExpr: (funcCall | identifier | arrayInit | BOOLLIT | LB expr RB) DOT (funcCall | identifier index* | methodCallExpr) ;

methodCall: identifier index* DOT expr SEMICOLON? ;

expr8: LB expr RB | literal | arrayInit ;

arrayInit: arrayType arrayLit? ;

literal: 
    INTLIT | DECIMAL | BINARY | OCTAL | HEXADECIMAL | FLOATLIT | BOOLLIT | STRINGLIT 
  | structLit | identifier | NIL ;

arrayLit: LC (literal | arrayLit) literalTail RC literalTail ;

literalTail: COMMA (literal | arrayLit) literalTail | ;

structLit: identifier LC structElement? RC ;

structElement: identifier COLON expr elementTail ;
elementTail: COMMA structElement | ;

identifier: ID | 'value' | 'index' ;
endStmt: NL | SEMICOLON | SEMICOLON NL ;

// LEXICAL

// White spaces

WS : [ \t\f\r]+ -> skip ; // skip spaces, tabs

// Newline

NL: '\r'? '\n' {
    if self.preType in [self.ID, self.INTLIT, self.FLOATLIT, self.STRINGLIT, self.BOOLLIT, self.RETURN, self.BREAK, self.CONTINUE, self.RB, self.RC, self.RP, self.NIL, self.STRING, self.INT, self.FLOAT, self.BOOLEAN]: self.text = ';'
    else: self.skip()
};

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
DOT: '.' ;

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
INITOP: '=' ;
ASSIGN: ':=' ;
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

BOOLLIT: TRUE | FALSE ;
TRUE: 'true' ;
FALSE: 'false' ;

// Identifier

ID: [a-zA-Z_] [a-zA-Z_0-9]* ;

// Literals

INTLIT:
    DECIMAL
|   BINARY
|   OCTAL
|   HEXADECIMAL
;

FLOATLIT:
    [0-9]+ DOT [0-9]*
|   [0-9]+ DOT [0-9]* ('e'|'E') ('+'|'-')? [0-9]+
;

DECIMAL:
    [0-9]
|   [1-9] [0-9]+
;

HEXADECIMAL: '0' ('x'|'X') [0-9a-fA-F]+ ;

BINARY: '0' ('b'|'B') ('1'|'0')+ ;

OCTAL: '0' ('o'|'O') [0-7]+ ;

STRINGLIT: '"' ('\\' [ntr"\\] | ~["\\\r\n])* '"' ;

// Comment

fragment COMMENT_CONTENT: ( ~[*] | '*' ~[/] | COMMENT )*;

COMMENT: (('//' ~[\r\n]* ) | ('/*' COMMENT_CONTENT '*/')) -> skip ;

ILLEGAL_ESCAPE: '"' ('\\' [ntr"\\] | ~["\\])* ('\\' ~[tnr"\\] | '\\') { raise IllegalEscape(self.text) };
UNCLOSE_STRING: '"' ([#-~ !]| [\b\f\t] | ('\'' '"'))* {
    raise UncloseString(self.text)
};
ERROR_CHAR: . {raise ErrorToken(self.text)} ;
