from ply import lex

tokens = [
    'ID',
    'NUMBER',
    'PLUS',
    'MINUS',
    'MUL',
    'DIV',
    'POW',
    'LPAR',
    'RPAR',
    'SEP',
    'ASSIGN',
    'SQRT',
    'PRINT',
    'PI'
]

t_PLUS  = r'\+'
t_MINUS = r'-'
t_MUL   = r'\*'
t_DIV   = r'/'
t_POW   = r'\^'
t_LPAR  = r'\('
t_RPAR  = r'\)'
t_ASSIGN = r'='
t_SEP = r';'

def t_SQRT(t):
    r'sqrt\b'
    return t

def t_PRINT(t):
    r'print\b'
    return t

def t_PI(t):
    r'pi\b'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_NUMBER(t):
    r'[1-9]+[.]?\d*|[0]?\.\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        t.value = float(t.value)
    return t

t_ignore  = ' \t\n'

def t_error(t):
     print("Illegal character '%s'" % t.value[0])
     t.lexer.skip(1)

lexer = lex.lex()
