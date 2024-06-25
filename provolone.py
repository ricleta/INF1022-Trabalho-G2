import ply.lex as lex
import ply.yacc as yacc

# Lexer tokens
tokens = (
    'INICIO', 'MONITOR', 'EXECUTE', 'TERMINO', 
    'ENQUANTO', 'FACA', 'FIM', 'ID', 'NUMERO',
    'PLUS', 'EQUAL', 'MULT', 'DIV', 'MINUS',
    'IF', 'THEN', 'ELSE', 
    'ZERO', 'EVAL', 'VEZES', 
    'COMPARE', 'GREATER', 'LESSER',
    'END_IF', 'OPEN_PAREN', 'CLOSE_PAREN',
)

# Token definitions (regexs)
t_INICIO = r'INICIO'
t_MONITOR = r'MONITOR'
t_EXECUTE = r'EXECUTE'
t_TERMINO = r'TERMINO'
t_ENQUANTO = r'ENQUANTO'
t_FACA = r'FACA'
t_FIM = r'FIM'
t_IF = r'IF'
t_END_IF = r'END_IF'
t_THEN = r'THEN'
t_ELSE = r'ELSE'
t_ZERO = r'ZERO'
t_EVAL = r'EVAL'
t_VEZES = r'VEZES'
t_COMPARE = r'=='
t_GREATER = r'>'
t_LESSER = r'<'
t_PLUS = r'\+'
t_MINUS = r'-'
t_EQUAL = r'='
t_MULT = r'\*'
t_DIV = r'/'
t_NUMERO = r'\d+'
t_OPEN_PAREN = r'\('
t_CLOSE_PAREN = r'\)'

monitored_vars = dict()

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
    'IF': 'IF',
    'THEN': 'THEN',
    'ELSE': 'ELSE',
    'ZERO': 'ZERO',
    'EVAL': 'EVAL',
    'VEZES': 'VEZES',
    'COMPARE': 'COMPARE',
    'GREATER': 'GREATER',
    'LESSER': 'LESSER',
    'END_IF': 'END_IF',
    'OPEN_PAREN': 'OPEN_PAREN',
    'CLOSE_PAREN': 'CLOSE_PAREN',
}

# Error handling for unknown characters
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Define operator precedence and associativity
'''
Necessário para remover conflitos shift/reduce em arithmetic_expr, 
mais detalhes no relatório
'''
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULT', 'DIV'),
)

# Grammar rules
def p_programa(p):
    '''programa : INICIO varlist MONITOR idlist EXECUTE cmds TERMINO '''
    show_monitored = "// Monitored vars = "
    for var in monitored_vars:
        show_monitored += f" {var[0]}"
    for var in monitored_vars:
        show_monitored += f'\nprintf("{var[0]} = %d\\n", {var[0]})'
    show_monitored += "\n"
    
    p[0] = f"#include <stdio.h>\nint main() {{\n{p[2]}\n{show_monitored}\n{p[6]}\nreturn 0;\n}}"

def p_cmds(p):
    '''cmds : cmd cmds
            | cmd'''
    for cmd in p[1:]:
        if cmd is not None and p[0] is None:
            p[0] = cmd
        elif cmd is not None:
            p[0] += cmd

def p_cmd(p):
    ''' cmd : while_statement
            | assignment
            | conditional
            | zero_statement
            | eval_statement
    '''
    p[0] = f"{p[1]};"
    for var in monitored_vars:
        if monitored_vars[var] == 1:
            p[0] += f"\nprintf(\"{var} = %d\\n\", {var});\n"
            monitored_vars[var] = 0

def p_term(p):
    '''term : ID 
            | NUMERO
    '''
    p[0] = p[1]
    
def p_assignment(p):
    ''' assignment : ID EQUAL arithmetic_expr
    '''
    p[0] = f"{p[1]} = {p[3]}"
    if p[1] in monitored_vars:
        monitored_vars[p[1]] = 1

def p_arithmetic_expr(p):
    ''' arithmetic_expr : arithmetic_expr PLUS arithmetic_expr
                        | arithmetic_expr MULT arithmetic_expr
                        | arithmetic_expr MINUS arithmetic_expr
                        | arithmetic_expr DIV arithmetic_expr
                        | OPEN_PAREN arithmetic_expr CLOSE_PAREN
                        | term
    '''
    if len(p) == 4 and p[1] == '(' and p[3] == ')':
        p[0] = f"({p[2]})"
    elif len(p) == 4:
        p[0] = f"{p[1]} {p[2]} {p[3]}"
    else:
        p[0] = p[1]
 
def p_conditional(p):
    ''' conditional : IF condicao THEN cmds END_IF
                    | IF condicao THEN cmds ELSE cmds END_IF'''
    if len(p) == 6:
        p[0] = f"\nif ({p[2]}) {{\n{p[4]}\n}}"
    else:
        p[0] = f"\nif ({p[2]}) {{\n{p[4]}\n}} else {{\n{p[6]}\n}}" 

def p_while_statement(p):
    ''' while_statement : ENQUANTO condicao FACA cmds FIM '''
    p[0] = f"while ({p[2]}) {{\n{p[4]}\n}}"

def p_zero_statement(p):
    ''' zero_statement : ZERO OPEN_PAREN ID CLOSE_PAREN'''
    p[0] = f"\n{p[3]} = 0"
    if p[3] in monitored_vars:
        monitored_vars[p[3]] = 1

def p_eval_statement(p):
    ''' eval_statement : EVAL cmds VEZES arithmetic_expr FIM 
    '''
    p[0] = f"for (int i = 0; i < {p[4]}; i++) {{\n{p[2]}\n}}"

def p_varlist(p):
    '''varlist : ID varlist
                | ID'''
    for var in p[1:]:
        if var is not None and p[0] is None:
            p[0] = f"int {var} = 0;\n"
        elif var is not None:
            p[0] += f"{var}"

def p_condicao(p):
    '''condicao : arithmetic_expr COMPARE arithmetic_expr
                | arithmetic_expr GREATER arithmetic_expr
                | arithmetic_expr LESSER arithmetic_expr
    '''
    p[0] = f"{p[1]} {p[2]} {p[3]}"

def p_idlist(p):
    '''idlist : ID idlist
              | ID'''
    if len(monitored_vars) == 0 and p[0] is None:
        monitored_vars[p[1]] = 0
    else:
        monitored_vars[p[1]] = 0
    
def p_error(p):
    print(f"Syntax error at '{p.value}'")

# Build the lexer and parser
lexer = lex.lex()
parser = yacc.yacc()

teste_file_name = input("Digite o nome do arquivo de teste (sem o .txt): ")
in_file = open(f"testes/{teste_file_name}.txt", "r").read()
out_file = open(f"results/{teste_file_name}.c", "w")

# Parse input program
lexer.input(in_file)

out_text = parser.parse(in_file)
out_file.write(out_text)

out_file.close()