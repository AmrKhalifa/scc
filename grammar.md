# Grammar

This file is contains all the currently implemented grammar.

%tokens LPAREN RPAREN OPENCURLY CLOSECURLY SEMICOLON COMA EOF WHILE BREAK SWITCH CASE COLON DEFAULT EQAULS
%tokens VOID INT
%tokens RETURN
%tokens INTEGER ID PLUS MINUS MUL DIV STRING
%tokens BIG LESS
%tokens BIGEQ LESSEQ
%tokens INTEGER STRING ID PLUS MINUS MUL DIV


*tokens IF ELSE WHILE BREAK

ret_type: VOID

program : (funcdef)* EOF

funcdef : type_spec ID LPAREN RPAREN scope_block

scope_block: OPENCURLY (statement)* CLOSECURLY

statement : (funccall SEMICOLON)
            | (RETURN SEMICOLON)
            | scope_block
            | (var_assignment SEMICOLON)
            | (var_decl SEMICOLON)
            | SEMICOLON
            | ifstatement
            | while_statement
            | (BREAK SEMICOLON)
            | for_statement
            | switch_statement

while_statement : WHILE LPAREN expression RPAREN statement

for_statement : FOR LPAREN expression (COMA expression)* SEMICOLON expression SEMICOLON expression (COMA expression)*
RPAREN statement

switch_statement : SWITCH LPAREN expression RPAREN OPENCURLY case_statement* (DEFAULT COLON statement*)? CLOSECURLY

case_statement : CASE expression COLON statement*


var : ID

var_decl: var_type var_identifier_decl (COMA var_identifier_decl)*

var_identifier_decl: (var | var_assigment)

ifstatement: IF LPAREN expression RPAREN statement (ELSE statement)?

var_assignemnt: var EQUALS expression


var_type: INT

funccall : ID LPAREN ((expression (COMA expression)*) | empty) RPAREN
<<<<<<<<<<<<<<<<<<<<<<< MASTER
expression   : term ((PLUS | MINUS) term)*
term   : factor ((MUL | DIV) factor)*
factor :(PLUS|MINUS)factor | INTEGER |  string | funccall | (LPAREN expression RPAREN) | var
string : DOUBLE_QUOTE (CHAR | ESCAPED_CHAR)* DOUBLE_QUOTE

===============================
relationaleq : comp ((BIGEQ | LESSEQ) comp)*
comp : operation ((BIG | LESS) operation)*
operation : term ((PLUS | MINUS) term)*
term   : factor ((MUL | DIV) factor)*
factor :(PLUS|MINUS)factor | INTEGER |  string | funccall | LPAREN expression RPAREN
string : DOUBLE_QUOTE (CHAR | ESCAPED_CHAR)* DOUBLE_QUOTE

HEAD >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>