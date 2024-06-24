import ply.lex as lex
import ply.yacc as yacc

# Lexer tokens
tokens = (
    'INICIO', 'MONITOR', 'EXECUTE', 'TERMINO', 
    'ENQUANTO', 'FACA', 'FIM', 
    'OUT', 'ID', 'NUMERO',
    'PLUS', 'EQUAL', 'MULT', 
    'IF', 'THEN', 'ELSE', 
    'ZERO', 'EVAL', 'VEZES', 
    'COMPARE', 'GREATER', 'LESSER',
    'END_IF'
)

# Token definitions (regexs)
t_INICIO = r'INICIO'
t_MONITOR = r'MONITOR'
t_EXECUTE = r'EXECUTE'
t_TERMINO = r'TERMINO'
t_ENQUANTO = r'ENQUANTO'
t_FACA = r'FACA'
t_FIM = r'FIM'
t_OUT = r'OUT'
t_IF = r'IF'
t_END_IF = r'END_IF'
t_THEN = r'THEN'
t_ELSE = r'ELSE'
t_ZERO = r'ZERO'
t_EVAL = r'EVAL'
t_VEZES = r'VEZES'
t_COMPARE = r'=='
t_GREATER = r'GREATER'
t_LESSER = r'LESSER'
t_PLUS = r'\+'
t_EQUAL = r'='
t_MULT = r'\*'
t_NUMERO = r'\d+'

# Identifier (ID) token definition
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# Ignored characters (spaces and tabs)
t_ignore = ' \t\n'

# Reserved keywords mapping (for ID token)
reserved = {
    'INICIO': 'INICIO',
    'MONITOR': 'MONITOR',
    'EXECUTE': 'EXECUTE',
    'TERMINO': 'TERMINO',
    'ENQUANTO': 'ENQUANTO',
    'FACA': 'FACA',
    'FIM': 'FIM',
    'OUT': 'OUT',
    'IF': 'IF',
    'THEN': 'THEN',
    'ELSE': 'ELSE',
    'ZERO': 'ZERO',
    'EVAL': 'EVAL',
    'VEZES': 'VEZES',
    'COMPARE': 'COMPARE',
    'GREATER': 'GREATER',
    'LESSER': 'LESSER',
    'END_IF': 'END_IF'
}

# Error handling for unknown characters
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Precedence and associativity of operators
precedence = (
    ('left', 'PLUS'),
    ('left', 'MULT'),
)

# Grammar rules
def p_programa(p):
    '''programa : INICIO varlist MONITOR varlist EXECUTE cmds TERMINO '''
    p[0] = f"#include <stdio.h>\nint main() {{\n{p[2]}\n{p[4]}\n{p[6]}\nreturn 0;\n}}"
    print(f"Programa reconhecido: {p[0:]}")

def p_cmds(p):
    '''cmds : cmd cmds
            | empty'''
    for cmd in p[1:]:
        if cmd is not None and p[0] is None:
            p[0] = cmd
        elif cmd is not None:
            p[0] += cmd
    print(f"Cmds reconhecido {p[0:]}")

def p_cmd(p):
    ''' cmd : ENQUANTO ID FACA cmds FIM
            | assignment
            | arithmetic_expr
            | conditional
            | zero_statement
            | eval_statement
            | out_statement
    '''
    p[0] = f"{p[1]};"
    print(f"Cmd reconhecido {p[0:]}")

def p_assignment(p):
    ''' assignment : ID EQUAL ID 
                    | ID EQUAL NUMERO 
                    | ID EQUAL arithmetic_expr
    '''
    print(f"Antes de p[0] assignment reconhecido {p[0:]}")
    p[0] = f"{p[1]} = {p[3]}"
    print(f"Assignment reconhecido {p[0:]}")

def p_arithmetic_expr(p):
    ''' arithmetic_expr : ID PLUS ID 
                        | ID PLUS NUMERO 
                        | NUMERO PLUS ID
                        | ID MULT ID 
                        | ID MULT NUMERO 
                        | NUMERO MULT ID '''
    p[0] = f"{p[1]} {p[2]} {p[3]}"
    print(f"Expressão aritmética reconhecida {p[0:]}")

def p_conditional(p):
    ''' conditional : IF condicao THEN cmds END_IF
                    | IF condicao THEN cmds ELSE cmds END_IF'''
    if len(p) == 6:
        p[0] = f"\nif ({p[2]}) {{\n{p[4]}\n}}"
    else:
        p[0] = f"\nif ({p[2]}) {{\n{p[4]}\n}} else {{\n{p[6]}\n}}" 
    print(f"Condicional reconhecido {p[0:]}")

def p_zero_statement(p):
    ''' zero_statement : ZERO ID '''
    p[0] = f"{p[2]} = 0;"
    print(f"Zero statement reconhecido {p[0:]}")

def p_eval_statement(p):
    ''' eval_statement : EVAL cmds VEZES arithmetic_expr FIM 
                       | EVAL cmds VEZES ID FIM '''
    print(f"Eval statement reconhecido {p[0:]}")

def p_out_statement(p):
    ''' out_statement : OUT ID '''
    print(f"Out statement reconhecido {p[0:]}")

def p_varlist(p):
    '''varlist : ID varlist
                | ID'''
    for var in p[1:]:
        if var is not None and p[0] is None:
            p[0] = f"int {var} = 0;\n"
        elif var is not None:
            p[0] += f"{var}"
    print(f"Varlist reconhecida {p[0:]}")

def p_condicao(p):
    '''condicao : ID COMPARE ID
                | ID GREATER ID
                | ID LESSER ID
                | ID COMPARE NUMERO
                | ID GREATER NUMERO
                | ID LESSER NUMERO'''
    p[0] = f"{p[1]} {p[2]} {p[3]}"
    print(f"Condição reconhecida {p[0:]}")

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    print(f"Syntax error at '{p.value}'")

# Build the lexer and parser
lexer = lex.lex()
parser = yacc.yacc()

in_file = open("testes/teste0.txt", "r").read()
out_file = open("results/teste0.c", "w")

# Parse input program
lexer.input(in_file)
# for token in lexer:
    # print(token)

out_text = parser.parse(in_file)
out_file.write(out_text)

out_file.close()
