from ply import yacc
import sys, json, pprint, re

from scanner import tokens

# OPCODES
EMPTY = 0
NUM = 1
ID = 2
SEQ = 3
ASSIGN = 4
PLUS = 5
MINUS = 6
UNARYMINUS = 7
MUL = 8
DIV = 9
POW = 10
PRINT = 20
SQRT = 30

def p_program_exp(p):
    'program : statement_list'
    p[0] = p[1]
    
def p_statement_list(p):
    'statement_list : statement_list SEP statement'
    p[0] = (SEQ,p[1],p[3])
    
def p_statement(p):
    'statement_list : statement'
    p[0] = p[1]
    
def p_statement_empty(p):
    'statement : '
    p[0] = (EMPTY,)
    
def p_statement_ass(p):
    'statement : assignment'
    p[0] = p[1]
    
def p_statement_expr(p):
    'statement : expression'
    p[0] = p[1]
    
def p_statement_print(p):
    'statement : printstmt'
    p[0] = p[1]
    
def p_assignment(p):
    'assignment : ID ASSIGN expression'
    p[0] = (ASSIGN,p[1],p[3])
    
def p_print(p):
    'printstmt : PRINT LPAR expression RPAR'
    p[0] = (PRINT, p[3])

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = (PLUS, p[1], p[3])

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = (MINUS, p[1], p[3])

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term MUL power'
    p[0] = (MUL, p[1], p[3])

def p_term_div(p):
    'term : term DIV power'
    p[0] = (DIV, p[1], p[3])

def p_term_power(p):
    'term : power'
    p[0] = p[1]
    
def p_power_raise(p):
    'power : factor POW power'
    p[0] = (POW, p[1], p[3])

def p_power_factor(p):
    'power : factor'
    p[0] = p[1]

def p_factor_id(p):
    'factor : ID'
    p[0] = (ID,p[1])

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = (NUM,p[1])

def p_factor_expr(p):
    'factor : LPAR expression RPAR'
    p[0] = p[2]
    
def p_factor_neg(p):
    'factor : MINUS factor'
    p[0] = (UNARYMINUS, p[2])

def p_factor_pi(p):
    'factor : PI'
    p[0] = p[1]
    
def p_factor_sqrt(p):
    'factor : SQRT LPAR expression RPAR'
    p[0] = (SQRT, p[3])

def p_error(p):
    print("Syntax error in input!")

def help(s):
    print(f"Uso: ./{s} [opzioni] -p input_prog | -f prog_file")
    print("OPTIONS: ")
    print("\t-h: stampa questo help e termina")
    print("\t-t: stampa su stdout l'Abstract Syntax Tree")
          
def main():
    # Nome del programmma
    name_program = re.sub('^.*/','', sys.argv[0])
    
    if len(sys.argv) < 3:
        help(name_program)
        sys.exit()
        
    # Default param
    print_ast = False 
    
    i = 1
    while i < len(sys.argv) - 2:
        tok = sys.argv[i]
        if tok == '-h':
            help(name_program)
            sys.exit()
        elif tok == '-t':
            print_ast = True
        i += 1
        
    if sys.argv[i] not in {'-p', '-f'}:
        help(name_program)
        sys.exit()

    # Lettura del programma
    if sys.argv[i] == "-p":
        program = sys.argv[i + 1]
        file_out = "ast.json"
    else:
        with open(sys.argv[i + 1]) as file:
            program = file.read()
        file_out = re.sub('^(.*).LD', '\\1.json', sys.argv[i+1])
        if file_out == sys.argv[i + 1]:
            file_out = "ast.json" 

    # Istanziazione del parser/compilatore
    parser = yacc.yacc()

    # Creazione dell'ast
    ast = parser.parse(program)

    # Stampa di controllo dell'AST
    if print_ast:
        print("Abstract Syntax Tree internal representation")
        pp = pprint.PrettyPrinter(width=40, compact=True)
        pp.pprint(ast)

    # Scrittura del file 
    if ast is not None:
        json_file = json.dumps(ast)
        with open(file_out,'w') as file:
            file.write(json_file)


if __name__ == '__main__':
    main()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
