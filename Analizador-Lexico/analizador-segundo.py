import ply.lex as lex
import re
import codecs
import os
import sys 

# Lista de tokens
tokens = [ 
            'IDENTIFICADOR',
            'NUMBER',
            'PARENTESIS_LEFT',
            'PARENTESIS_RIGHT',
            'LLAVE_LEFT',
            'LLAVE_RIGHT',
            'SUMA', 
            'RESTA', 
            'MULTIPLICACION', 
            'DIVISION',
            'MODULO', 
            'FIN_DE_INSTRUCCION', 
            'PUNTO_Y_COMA',
            'MAYOR_QUE',
            'MENOR_QUE',
            'MAYOR_IGUALL_QUE',
            'MENOR_IGUAL_QUE', 
            'DIFERENTE_DE', 
            'ASIGNACION', 
            'COMPARACION', 
            'AND', 
            'OR', 
            'NOT', 
            'NUMERAL',
            'COMENTARIOS_UNA_LINEA',
            'COMENTARIOS_VARIAS_LINEAS',
            'COMILLAS',
            'APOSTROFES',
            'PUNTO',
            'COMA',
            'NUMERAL',
            'MAS_MAS',
            'MENOS_MENOS',
            'MAYOR_ESCRIBIR_MOSTRAR',  #caracteres que utilizamos en C++ como cout<<
            'MENOR_OBTENER_ALMACENAR', #caracteres que utilizamos en C++ para recibir cin>>
            'ERROR'

]

# Diccionario de palabras reservadas

palabrasReservadas = {

    'include':'INCLUDE',
    'using':'USING',
    'namespace':'NAMESPACE',
    'std':'STD',
    'cout':'COUT',
    'cin':'CIN',
    'main' : 'MAIN',
    'endl':'ENDL',
    'if':'IF',
    'else':'ELSE',
    'int':'INT',
    'float':'FLOAT',
    'string':'STRING',
    'char':'CHAR',
    'bool':'BOOL',
    'const':'CONST',
    'void':'VOID',
    'do':'DO',
    'while':'WHILE',
    'for':'FOR',
    'switch':'SWITCH',
    'break':'BREAK',
    'try':'TRY',
    'catch':'CATCH',
    'return':'RETURN',
    'private':'PRIVATE',
    'public':'PUBLIC',
    'default':'DEFAULT',
    'delete':'DELETE',
    'true':'TRUE',
    'false':'FALSE'
}

#unimos el array y el diccionario

tokens = tokens + list(palabrasReservadas.values())

#DEFINIENDO CADA EXPRESION REGULAR, ESTOY EVALUANDO SU FORMATO, NO UNA COINCIDENCIA EXACTA
#EXPRESIONES REGUALES PARA SÍMBOLOS ESPECIALES DE CARACTER SIMPLE
t_ignore = '\t'
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_MODULO = r'\%'
t_ASIGNACION = r'='
t_PARENTESIS_LEFT = r'\('
t_PARENTESIS_RIGHT = r'\)'
t_LLAVE_LEFT = r'\{'
t_LLAVE_RIGHT = r'\}'
t_DOS_PUNTOS = r':'
t_PUNTO = r'\.'
t_COMA = r',' 
t_MAYOR_QUE = r'>'
t_MENOR_QUE = r'<'
t_MAYOR_IGUAL_QUE = r'>='
t_MENOR_IGUAL_QUE = r'<='
t_DIFERENTE_DE = r'!='
t_COMPARACION = r'=='
t_AND = r'\&\&'
t_OR = r'\|\|'
t_NOT = r'\!'
t_COMILLAS = r'\" '
t_APOSTROFE_LEFT = r'\''



#Definiendo expresiones regulares para caracteres ESPECIALES COMPLEJOS 
#caracteres especiales identificador, comentarios, etc 

def t_IDENTIFICADOR(t):
    r'[a-zA-Z0-9_]*' #esto es lo que reconoce un identificador
    if t.value.upper() in palabrasReservadas:
        t.value = t.value.upper()
        t.type = t.value
    return t

def t_NUMBER(t):
    r'\d+' #la d son los numeros del 1 al 9 en el lenguaje de expresiones regualares y el signo + representa que puede ir cualquier numero 1 o más veces 
    t.value = t.value #unicamente reconoce los digitos enteros
    return t

def t_FLOAT(t):
    r'\d+[^.]+\d' #reconoce numeros flotantes o decimales 
    return t

def t_STRING(t):

    r'\"?(\w+ \ *\w*\d* \ *)\"?' #expresion regular para reconocer los STRING
    return t 

def t_NUMERAL(t):
    r'\#'
    return t

def t_MAS_MAS(t):
    r'\+\+'
    return t

def t_MENOS_MENOS(t):
    r'\-\-'
    return t

def t_COMENTARIOS_UNA_LINEA(t):
    r'\/\/.*' #no devuelve un valor, reconoce que es un comentario pero obvia la función y no devuelve nada
    pass

def t_COMENTARIOS_VARIAS_LINEAS(t):
    r'\/\*\[a-zA-Z0-9_\s]*\*\/ | \*\/.*\*\/'   #no reconcoe las cadenas de caracteres de los comentarios, permite escribirlos pero los ignora
    pass #obviamos, reconoce el token pero no lo va devolver, es decir es ignorado. 


def t_FIN_DE_INSTRUCCION(t):
    r'\;'
    return t #esto es un cambio de linea 

def t_MAYOR_ESCRIBIR_MOSTRAR(t):
    r'\<\<'
    return t

def t_MENOR_OBTENER_ALMACENAR(t):
    r'\>\>'
    return t

def t_ERROR(t): #reconoce si un token es invalido

    print ("caracter ilegal '%s'") % t.value[0]
    t.lexer.skip(1)


def buscarFicheros(directorio):
    ficheros = []
    numeroArchivo = ''
    respuesta = False
    cont = 1

    for base, directorios, files in os.walk(directorio):
        ficheros.append(files)

    for file in files:  
        print (str(cont)+ ". "+ file)
        cont = cont + 1

    while respuesta == False:
        numeroArchivo = raw_input( '\n Numero de test: ')
        for file in files: 
            if file == files[int(numeroArchivo)-1]:
                respuesta == True
                break

    print ("Has escogido un archivo \" %s\" \n " %files[int(numeroArchivo)-1])

    return files[int(numeroArchivo)-1]



#ES PARA REALIZAR EL TEST

    directorio = open(r"C:\Users\Mendez Castillo\Desktop\Analizador_Lexico\Pruebas")
    archivo = buscarFicheros(directorio)
    test = directorio+archivo
    fileOpen = codecs.open(test, "r", "utf-8")
    cadena = fileOpen.read()
    fileOpen.close()

    analizadorLexico = lex.lex()
    analizadorLexico.input(cadena)

    while True:
        tok = analizadorLexico.token()
        if not tok : break
        print (tok)

input()