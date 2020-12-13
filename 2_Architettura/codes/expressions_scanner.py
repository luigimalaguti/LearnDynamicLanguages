from ply import lex

tokens = ('NUMBER','PLUS','MINUS','MUL','DIV','POW','LPAR','RPAR',)

t_PLUS  = r'\+'
t_MINUS = r'-'
t_MUL   = r'\*'
t_DIV   = r'/'
t_POW   = r'\^'          
t_LPAR  = r'\('
t_RPAR  = r'\)'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t
 
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = r' \t'

def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()