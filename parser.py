from automatas import *
from lex import *


prods = {
    'Programa':[
        ['ListaDecl', 'EOF']
    ],

    'ListaDecl':[
        ['Declaracion', 'ListaDecl2'],
        []
    ],

    'ListaDecl2':[
        ['Declaracion', 'ListaDecl2']
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
        ['ID', 'PAREN_OPEN', 'ListaParametros', 'PAREN_CLOSE', 'Bloque']
    ],

    'ListaParametros':[
        ['Parametros'],
        []
    ],

    'Parametros':[
        ['ID', 'Param']
    ],

    'Param':[
        ['COMA', 'ID', 'Param'],
        []
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
        ['Bloque'],
    ],

    'ExprSent':[
        ['Expresion', 'PUNTOCOMA']
    ],

    'Expresion':[
        ['Asignacion']
    ],

    'Asignacion':[
        ['ID', 'IGUAL', 'Primitivo'],
        ['OLogico', 'PUNTOCOMA'],
    ],

    'ForSent':[
        ['FOR', 'PAREN_OPEN', 'PriArg', 'AdicArg', 'PUNTOCOMA', 'AdicArg', 'PAREN_CLOSE', 'Sentencia']
    ],

    'PriArg':[
        ['VarDecl'],
        ['ExprSent'],
        ['PUNTOCOMA']
    ],

    'AdicArg':[
        ['Expresion'],
        []
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
        ['"while"', 'PAREN_OPEN', 'Expresion', 'PAREN_CLOSE', 'Sentencia']
    ],

    'Bloque':[
        ['LLAVE_ABIERTA', 'ListaSent', 'LLAVE_CERRADA']
    ],

    'ListaSent':[
        ['Sentencia', 'ListaSent'],
        [],
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
        ['Comparacion', 'A_ExclamacionIgual', 'Igua']
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
                'ListaSent',
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
        pni('Programa')
        token_actual = self['tokens'][self['index']]
        print('tiene que comparar', token_actual[0], 'EOF',self['error'])
        if self['error'] or token_actual[0]!='EOF':
            print('Cadena no aceptada')
            return False
        else:
            print('Cadena aceptada')
            return True

    def procesar(parteDerecha):
        if parteDerecha == '':
            self['index'] += 1
            return
        for simbolo in parteDerecha:
            token_actual = self['tokens'][self['index']]
            print("token actual", token_actual)
            self['error'] = False
            print('en procesar simbolo a evaluar:', simbolo, 'con', token_actual[0])
            if es_Terminal(simbolo):
                print('en procesar', simbolo, 'es terminal')
                if simbolo == token_actual[self['index']]: # si simbolo es igual al primer elemento de la tupla token_actual
                    print(("avanzo con", simbolo, self))
                    self['index'] += 1
                    print("el indice vale", self['index'])
                else:
                    self['error'] = True
                    break
            elif es_No_Terminal(simbolo):
                print('en procesar', simbolo, 'es un no terminal')
                pni(simbolo)
                if self['error']:
                    break

    def pni(noTerminal):
        for parteDerecha in prods[noTerminal]:
            print("en pni entra", parteDerecha)
            index_aux = self['index'] #Pivote de retroceso
            procesar(parteDerecha)
            if self['error'] == True:
                print('en pni Error entonces hace BackTracking')
                self['index'] == index_aux
            else:
                break


    return parse()


cases = [
    ('', True),
    #('if(id) id ;', True),
    #('var id;', True),
    #('var id = True ;', True)
]


for cadena, resultado in cases:
    assert parser(cadena) == resultado


