import ply.lex as lex

resul_lexema = []

reservada = (
     'INCLUDE',
     'USING',
     'NAMESPACE',
     'STD',
     'COUT'
     'CIN',
     'GET',
     'CADENA',
     'RETURN',
     'VOID',
     'INT',
     'ENDL',
)

tokens = reservada + (
     'IDENTIFICADOR',
     'ENTERO',
     'ASIGNAR',

     'SUMA',
     'RESTA',
     'MULT',
     'DIV',
     'POTENCIA',
     'MODULO',

     'MINUSMINUS',
     'PLUSPLUS',

    # Condiones
     'SI',
     'SINO',

    # Ciclos
     'MIENTRAS',
     'PARA',

    # Logica
     'AND',
     'OR',
     'NOT',
     'MENORQUE',
     'MAYORQUE',    # Agregado
     'MENORIGUAL',  # Comprobar en las reglas
     'MAYORIGUAL',
     'IGUAL',
     'DISTINTO',

    # Simbolos
     'NUMERAL',

     'PARIZO',
     'PARDER',
     'CORIZO',
     'CORDER',
     'LLAIZO',
     'LLADER',

    # Otros
     'PUNTOCOMA',
     'COMA',
     'COMDOB',
     'MAYORDER',   # >>          
     'MAYORIZO',   # <<
)

# Reglas de Expresiones Regulares para token de contexto simple

# PUNTO = r'\.'

t_ASINAR = r'\='

t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULT = r'\*'
t_DIV = r'/' # Puede confunsirse la division, para aclarar se usa: /
t_POTENCIA = r'(\*{2} | \^)'  # Revisar
t_MODULO = r'\%'

t_MINUSMINUS = r'\-\-'
t_PLUSPLUS = r'\+\+'

t_AND = r'\&\&'
t_OR = r'\|{2}' # Revisar
t_NOT = r'\!'
t_MENORQUE = r'\<'
t_MAYORQUE = r'\>'

# Agregado para ampliar reglas
t_MENORIGUAL = r'\=\<'
t_MAYORIGUAL = r'\=\>'
t_IGUAL = r'\=\='
t_DISTINTO = r'\=\!'

t_PUNTOCOMA = r'\;'
t_COMA = r'\,'
t_COMDOB = r'\"'

# Comprobar que lo siguiente este en los tokens
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'

# Comprobar en ejecucion
t_LLAIZQ = r'{'   # LLAIZQ = r'\{' 
t_LLADER = r'}'   # LLAIZQ = r'\}'

def t_INCLUDE(t):
    r'include'
    return t

def t_USING(t):
    r'using'
    return t

def t_NAMESPACE(t):
    r'namespace'
    return t

def t_STD(t):
    r'std'
    return t

def t_COUT(t):
    r'cout'
    return t

def t_CIN(t):
    r'cin'
    return t

def t_GET(t):
    r'get'
    return t

def t_ENDL(t):
    r'endl'
    return t

def t_SINO(t):
    r'else'
    return t

def t_SI(t):
    r'if'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_VOID(t):
    r'void'
    return t

def t_MIENTRAS(t):
    r'while'
    return t

def t_PARA(t):
    r'for'
    return t

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IDENTIFICADOR(t):
    r'\w+(_\d\w)*'
    return t

def t_CADENA(t):
    r'\"?(\w+ \ *\w*\d* \ *)\"?'
    return t

def t_NUMERAL(t):
    r'\#'
    return t

def t_PLUSPLUS(t):
    r'\+\+'
    return t