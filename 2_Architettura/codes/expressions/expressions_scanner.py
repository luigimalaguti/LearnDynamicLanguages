from ply import lex

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'MUL',
    'DIV',
    'POW',
    'LPAR',
    'RPAR',
    'SQRT',
    'PI',
    'ASSIGN',
    'ID'
)

t_PLUS  = r'\+'
t_MINUS = r'-'
t_MUL   = r'\*'
t_DIV   = r'/'
t_POW   = r'\^'
t_LPAR  = r'\('
t_RPAR  = r'\)'
t_ASSIGN = r'='

def t_SQRT(t):
    r'sqrt\b'
    return t

def t_PI(t):
    r'pi\b'
    return t

def t_NUMBER(t):
    r'[1-9]+[.]?\d*|[0]?\.\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        t.value = float(t.value)
    return t

def t_ID(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()
