from ply import lex

# Token riservati
reserved = {
    'if'    : 'IF',
    'else'  : 'ELSE',
    'elif'  : 'ELIF',
    'while' : 'WHILE',
    'def'   : 'DEF',
    'return': 'RETURN'
}

# Lista dei token
tokens = [
    'ID', 'NUMBER', 'COLON', 'COMMA',
    'PLUS', 'MINUS', 'MUL', 'DIV',
    'AND', 'OR', 'NOT', 'LPAR', 
    'RPAR', 'SEP', 'EQ', 'NEQ', 
    'LT', 'GT', 'LE', 'GE',
    'ASSIGN', 'PRINT', 'PI'
] + list(reserved.values())

# Definizione dei token semplici
t_COLON = r':'
t_COMMA = r','
t_PLUS  = r'\+'
t_MINUS = r'-'
t_MUL   = r'\*'
t_DIV   = r'/'
t_LPAR  = r'\('
t_RPAR  = r'\)'
t_ASSIGN = r'='
t_SEP = r';'
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_EQ = r'=='
t_NEQ = r'!='
t_AND = r'and\b'
t_OR = r'or\b'
t_NOT = r'not\b'
t_PI = r'pi\b'
t_PRINT = r'print\b'

# Definizione dei token restanti
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')  # Controllo su parola chiave
    return t

def t_NUMBER(t):
    r'\d*\.\d+|\d+'
    v = float(t.value)
    if v == int(v):
        t.value = int(v)    
    else:
        t.value = v
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

def t_error(t):
     print("Illegal character '%s'" % t.value[0])
     t.lexer.skip(1)

def main():
    lexer = lex.lex()

    programma = """x = 10.23
    def square(num):
        return num * num"""

    lexer.input(programma)

    print(lexer)

    for token in lexer:
        print(token)

if __name__ == "__main__":
    main()