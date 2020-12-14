from ply import yacc
from math import pi, sqrt

from expressions_scanner import tokens

symbol_table = {}

def p_statement_assign(p):
    'statement : assignment'
    p[0] = p[1]

def p_statement_expr(p):
    'statement : expression'
    p[0] = p[1]

def p_assignment(p):
    'assignment : ID ASSIGN expression'
    symbol_table[p[1]] = p[3]
    p[0] = p[3]

def p_expression_add(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_sub(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_mul(p):
    'term : term MUL power'
    p[0] = p[1] * p[3]

def p_term_div(p):
    'term : term DIV power'
    p[0] = p[1] / p[3]

def p_term_power(p):
    'term : power'
    p[0] = p[1]

def p_power_raise(p):
    'power : factor POW power'
    p[0] = p[1]**p[3]
    
def p_power_factor(p):
    'power : factor'
    p[0] = p[1]
    
def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAR expression RPAR'
    p[0] = p[2]

def p_factor_pi(p):
    'factor : PI'
    p[0] = pi

def p_factor_sqrt(p):
    'factor : SQRT LPAR expression RPAR'
    p[0] = sqrt(p[3])

def p_factor_id(p):
    'factor : ID'
    v = symbol_table.get(p[1], None)
    if v is None:
        p_error(p)
    p[0] = v

def p_error(p):
    print("Syntax error in input!")


def main():
    parser = yacc.yacc()
    while True:
        try:
            s = input('calc (ctrl-d to quit) > ')
        except EOFError:
            break
        if not s: continue
        result = parser.parse(s)
        print(result)
