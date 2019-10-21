from automatas import *
from lex import *

prods = {
    'Programa':[
        ['ListaDecl', '"EOF"']
    ],

    'ListaDecl':[
        ['ListaDecl', 'Declaracion'],
        []
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
        [],
        ['Parametros']
    ],

    'Parametros':[
        ['ID'],
        ['Parametros', 'COMA', 'ID']
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
        [],
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

    'Primitvo':[
        ['TRUE'],
        ['FALSE'],
        ['Numero'],
        ['String'],
        ['ID'],
        ['PAREN_OPEN', 'Expresion', 'PAREN_CLOSE']
    ]

}

noTerminales = ['Programa',
                'ListaDecl',
                'Declaracion',
                'FunDecl',
                'Funcion',
                'ListaParametros',
                'Parametros',
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

def parser(tokens):
    
    self={
        'tokens': tokens,
        'index': 0,
        'error': False,
        }


    def parse():
        error = False
        index = 0
        pni('Programa')
        
        if not error == True and tokens(index) == "#":
            return True
        else:
            return False
    

    def procesar(parteDerecha):

        for simbolo in parteDerecha:
            if esTerminal(simbolo):
                if simbolo == tokens[index]:
                    index+=1
                else:
                    error = True
                    break

            if esNoTerminal(simbolo):
                pni(simbolo)
                if error == True:
                    break


    def pni(noTerminal):

        for parteDerecha in prods[noTerminal]:
            error = False
            index_aux = index
            procesar(parteDerecha)
            if error == False:
                break
            else:
                index = index_aux

    parse()


def esTerminal(simbolo):
    return True

def esNoTerminal(simbolo):
    return True