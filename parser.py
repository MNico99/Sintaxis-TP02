from automatas import *
from lex import *


prods = {
    'Programa':[
        ['ListaDecl', 'EOF'],
        ['EOF']
    ],

    'ListaDecl':[
        ['Declaracion'],
        ['ListaDecl2', 'Declaracion']
    ],

    'ListaDecl2':[
        ['Declaracion', 'ListaDecl2'],
        ['Declaracion']
    ],

    'Declaracion':[
        ['FunDecl'],
        ['VarDecl'],
        ['Sentencia']
    ],

    'FunDecl':[
        ['FUN', 'Funcion']
    ],

    'Funcion':[
        ['ID', 'PAREN_OPEN', 'ListaParametros', 'PAREN_CLOSE', 'Bloque'],
        ['ID', 'PAREN_OPEN', 'PAREN_CLOSE', 'Bloque']
    ],

    'ListaParametros':[
        ['Parametros']
    ],

    'Parametros':[
        ['ID', 'Param'],
        ['ID']
    ],

    'Param':[
        ['COMA', 'ID', 'Param']
    ],

    'VarDecl':[
        ['VAR', 'ID', 'PUNTOCOMA'],
        ['VAR', 'ID', 'IGUAL', 'Expresion', 'PUNTOCOMA']
    ],

    'Sentencia':[
        ['ExprSent'],
        ['ForSent'],
        ['IfSent'],
        ['ReturnSent'],
        ['WhileSent'],
        ['Bloque', 'PUNTOCOMA'],
    ],

    'ExprSent':[
        ['Expresion', 'PUNTOCOMA']
    ],

    'Expresion':[
        ['Asignacion']
    ],

    'Asignacion':[
        ['ID', 'IGUAL', 'Primitivo'],
        ['OLogico', 'PUNTOCOMA']
    ],

    'ForSent':[
        ['FOR', 'PAREN_OPEN', 'PriArg', 'AdicArg', 'PUNTOCOMA', 'AdicArg', 'PAREN_CLOSE', 'Sentencia'],
        ['FOR', 'PAREN_OPEN', 'PriArg', 'PUNTOCOMA', 'PAREN_CLOSE', 'Sentencia']
    ],

    'PriArg':[
        ['VarDecl'],
        ['ExprSent'],
        ['PUNTOCOMA']
    ],

    'AdicArg':[
        ['Expresion']
    ],

    'IfSent':[
        ['IF', 'PAREN_OPEN', 'Expresion', 'PAREN_CLOSE', 'Sentencia', 'ELSE', 'Sentencia'],
        ['IF', 'PAREN_OPEN', 'Expresion', 'PAREN_CLOSE', 'Sentencia']
    ],

    'ReturnSent':[
        ['RETURN', 'Expresion', 'PUNTOCOMA'],
        ['RETURN', 'PUNTOCOMA']
    ],

    'WhileSent':[
        ['WHILE', 'PAREN_OPEN', 'Expresion', 'PAREN_CLOSE', 'Sentencia']
    ],

    'Bloque':[
        ['LLAVE_ABIERTA', 'ListaDecl', 'LLAVE_CERRADA', 'PUNTOCOMA'],
        ['LLAVE_ABIERTA', 'LLAVE_CERRADA', 'PUNTOCOMA']
    ],

    'OLogico':[
        ['YLogico'],
        ['YLogico', 'OR', 'OLogico']
    ],

    'YLogico':[
        ['Igua'],
        ['Igua', 'AND', 'YLogico']
    ],

    'Igua':[
        ['Comparacion'],
        ['Comparacion', 'DOBLE_IGUAL', 'Igua'],
        ['Comparacion', 'EXCLAMACION_IGUAL', 'Igua']
    ],

    'Comparacion':[
        ['Suma'],
        ['Suma', 'MAYOR', 'Comparacion'],
        ['Suma', 'MAYOR_IGUAL', 'Comparacion'],
        ['Suma', 'MENOR', 'Comparacion'],
        ['Suma', 'MENOR_IGUAL', 'Comparacion']
    ],

    'Suma':[
        ['Mult'],
        ['GUION_MEDIO', 'Suma'],
        ['MAS', 'Suma']
    ],

    'Mult':[
        ['Unario'],
        ['SLASH', 'Mult'],
        ['ASTERISCO', 'Mult']
    ],

    'Unario':[
        ['EXCLAMACION', 'Unario'],
        ['GUION_MEDIO', 'Unario'],
        ['Primitivo']
    ],

    'Primitivo':[
        ['TRUE'],
        ['FALSE'],
        ['Numero'],
        ['String'],
        ['ID'],
        ['PAREN_OPEN', 'Expresion', 'PAREN_CLOSE']
    ]

}


no_Terminales = ['Programa',
                'ListaDecl',
                'ListaDecl2', # Agregado por eliminacion de recursividad izq
                'Declaracion',
                'FunDecl',
                'Funcion',
                'ListaParametros',
                'Parametros',
                'Param', # Agregado por eliminacion de recursividad izq
                'VarDecl',
                'Sentencia',
                'ExprSent',
                'Expresion',
                'Asignacion',
                'ForSent',
                'PriArg',
                'AdicArg',
                'IfSent',
                'ReturnSent',
                'WhileSent',
                'Bloque',
                'OLogico',
                'YLogico',
                'Igua',
                'Comparacion',
                'Suma',
                'Mult',
                'Unario',
                'Primitivo'
]


def es_Terminal(simbolo):
    return not es_No_Terminal(simbolo)
    

def es_No_Terminal(simbolo):
    return simbolo in no_Terminales


def parser(cadena):
    
    self = {
        'tokens': lex(cadena),
        'index': 0,
        'error': False
        }

    def parse():
        print(cadena)
        pni('Programa')
        if self['index'] == len(self['tokens']):
            self['index'] -= 1
        token_actual = self['tokens'][self['index']]
        #print('tiene que comparar', token_actual[0], 'EOF', self['error'])
        if self['error'] or token_actual[0]!='EOF':
            print('Cadena no aceptada')
            return False
        else:
            print('Cadena aceptada')
            return True

    def procesar(parteDerecha):
        for simbolo in parteDerecha:
            token_actual = self['tokens'][self['index']]
            #print("token actual", token_actual)
            self['error'] = False
            #print('en procesar simbolo a evaluar:', simbolo, 'con', token_actual[0])
            if es_Terminal(simbolo):
                #print('en procesar', simbolo, 'es terminal')
                if simbolo == token_actual[0]: # si simbolo es igual al primer elemento de la tupla token_actual
                    #print(("avanzo con", simbolo, self))
                    self['index'] += 1
                    #print("el indice vale", self['index'])
                else:
                    self['error'] = True
                    break

            elif es_No_Terminal(simbolo):
                #print('en procesar', simbolo, 'es un no terminal')
                pni(simbolo)
                if self['error']:
                    break

    def pni(noTerminal):
        for parteDerecha in prods[noTerminal]:
            #print("en pni entra", parteDerecha)
            index_aux = self['index'] #Pivote de retroceso
            procesar(parteDerecha)
            if self['error'] == True:
                #print('en pni Error entonces hace BackTracking')
                self['index'] = index_aux
            
            else:
                break


    return parse()


cases = [
    ('', True), #1
    ('if(id) id ;', False), #2
    ('var id;', True), #3
    ('fun id ( ) { var id ;};', True), #4
    ('fun id ( id ) { var id ;};', True), #5
    ('fun id ( id ) { var id ;}', False), #6
    ('fun;', False), #7
    ('var id = True ;', False), #8
    ('while ( id = True ) { } ; ;', True), #9
    ('for ( var id ; ; ) id = False ;', True) #10
]


for cadena, resultado in cases:
    assert parser(cadena) == resultado
    print('tests:',cadena, resultado)
