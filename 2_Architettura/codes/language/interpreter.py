import sys, operator, json
from math import sqrt

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

symbol_table = {}

# Binary operators
binops = {
    PLUS: operator.add,
    MINUS: operator.sub,
    MUL: operator.mul,
    DIV: operator.itruediv,
    POW: operator.pow
}

def interpreter(ast):
    '''
    Visita in postordine ed esegue gli opcode dell'AST 
    generato dal "compilatore" calcomp.py
    '''
    opcode = ast[0]
    if opcode == EMPTY:
        return
    elif opcode == NUM:
        return ast[1]
    elif opcode == PRINT:
        print(interpreter(ast[1]))
    elif opcode == SQRT:
        return sqrt(interpreter(ast[1]))
    elif opcode == UNARYMINUS:
        return -interpreter(ast[1])
    elif opcode == ASSIGN:
        symbol_table[ast[1]] = interpreter(ast[2])
    elif opcode == ID:
        try:
            return symbol_table[ast[1]]
        except KeyError:
            print(f"L'identificatore {ast[1]} è indefinito.\n")
            print("Errore non recuperabile.")
            sys.exit()
    elif opcode == SEQ:
        interpreter(ast[1])
        interpreter(ast[2])
    elif opcode in binops.keys():
        arg1 = interpreter(ast[1])
        arg2 = interpreter(ast[2])
        return binops[opcode](arg1,arg2)
    else: # non dovrebbe accadere
        print(f"opcode {opcode} non definito.\n")
        print("Errore non recuperabile.")
        sys.exit()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Non è stato specificato il file con l'AST (estensione json)")
        sys.exit()
    else:
        try:
            ast = json.loads(open(sys.argv[1]).read())
        except JSONDecodeError:
            print("Errore nel file json")
            sys.exit()
        interpreter(ast)