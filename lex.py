# -*- coding: utf-8 -*-
from automatas import *


TokenConfig = [
    ('IF', A_If),
    ('EOF', A_EOF),
    ('ELSE', A_Else),
    ('FALSE', A_False),
    ('FOR', A_FOR),
    ('FUN', A_FUN),
    ('RETURN', A_Return),
    ('TRUE', A_True),
    ('VAR', A_VAR),
    ('WHILE', A_While),
    ('PAREN_OPEN', A_ParenOpen),
    ('PAREN_CLOSE', A_ParenClose),
    ('APOSTROFO', A_Apostrofo),
    ('ASTERISCO', A_Asterisco),
    ('COMA', A_Coma),
    ('LLAVE_ABIERTA', A_LlaveAbierta),
    ('LLAVE_CERRADA', A_LlaveCerrada),
    ('EXCLAMACION', A_Exclamacion),
    ('GUION_MEDIO', A_Guionmedio),
    ('MAS', A_Mas),
    ('PUNTO', A_Punto),
    ('PUNTOCOMA', A_PuntoComa),
    ('SLASH', A_Slash),
    ('IGUAL', A_Igual),
    ('DOBLE_IGUAL', A_DobleIgual),
    ('EXCLAMACION_IGUAL', A_ExclamacionIgual),
    ('MENOR', A_Menor),
    ('MAYOR', A_Mayor),
    ('MAYOR_IGUAL', A_Mayorigual),
    ('MENOR_IGUAL', A_Menorigual),
    ('AND', A_AND),
    ('OR', A_OR),
    ("NUM", A_Num),
    ("STRING", A_String),
    ("ID", A_ID),
]



def lex(cadena):

    tokens = []
    index = 0
    start = 0

    while index < len(cadena):

        #Solución al problema del espacio
        c = cadena[index]
        if c.isspace():
            index+=1
            continue
        
        start = index
        posible_candidato = []
        candidatos = []
        lexeme = ""
        cadenaPrefijo = ""
        todosTrampa = False
        
        while not todosTrampa:
                todosTrampa = True
                lexeme  = cadenaPrefijo
                cadenaPrefijo = cadena[start: index + 1]
                candidatos = posible_candidato 
                posible_candidato = []

                for  tipoDeToken, automata in TokenConfig:
                    resultado = automata(cadenaPrefijo)
                    if resultado == RESULTADO_ACEPTADO:
                        posible_candidato.append(tipoDeToken)
                        todosTrampa = False
                    elif resultado == RESULTADO_NO_ACEPTADO:
                        todosTrampa = False 
                    elif index > len(cadena): #Solución al bucle del ultimo caracter
                        break

                index += 1

        index -= 1
        if len(candidatos) == 0:
            raise Exception("TOKEN NO ACEPTADO " + lexeme)
        else:
            tipoDeToken = candidatos[0]
            tokens.append((tipoDeToken, lexeme))
    
    tokens.append(('EOF', 'EOF'))
    return tokens


