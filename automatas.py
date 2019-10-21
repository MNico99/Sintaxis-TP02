# -*- coding: utf-8 -*-
TRAMPA = -1
RESULTADO_ACEPTADO = "ACEPTADO"
RESULTADO_TRAMPA = "TRAMPA"
RESULTADO_NO_ACEPTADO = "NO_ACEPTADO"

digito = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
simbolos = ["(", ")", ",", ";", "=", "{", "}", "=", "!", ">", "<", "-", "+", "/", "*", ".", "'"]

####################GRAMATICA LEXICA#####################

#delta Numeros
def d_Num(estado_anterior, caracter):
    if estado_anterior == 0 and caracter in digito:
        return 1
    if estado_anterior == 1 and caracter in digito:
        return 1
    if estado_anterior == 1 and caracter == ".":
        return 2
    if estado_anterior == 2 and caracter in digito:
        return 3
    if estado_anterior == 3 and caracter in digito:
        return 3

    
    return TRAMPA

#automata Numeros
def A_Num(cadena):
    Finales = [1, 3]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_Num(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo
    
    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

casosNum = [
    ("13", RESULTADO_ACEPTADO),
    ("2.69a8", RESULTADO_TRAMPA),
    ("1323234.3", RESULTADO_ACEPTADO),
    ("2522.9.99", RESULTADO_TRAMPA),
    (".0111", RESULTADO_TRAMPA),
    ("1.0000003", RESULTADO_ACEPTADO)
]

for cadena, resultado in casosNum:
    assert A_Num(cadena) == resultado

#################################################################

#delta String
def d_String(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "'":
        return 1
    if estado_anterior == 1 and caracter.isalpha():
        return 2
    if estado_anterior == 1 and caracter in digito:
        return 2    
    if estado_anterior == 2 and caracter.isalpha():
        return 2
    if estado_anterior == 2 and caracter in digito:
        return 2 
    if estado_anterior == 2 and caracter == "'":
        return 3

    
    return TRAMPA

#automata String
def A_String(cadena):
    Finales = [3]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_String(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo
    
    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

casosString = [
    ("'AAAdssGFKHFga111skgAHADSF'", RESULTADO_ACEPTADO),    
    ("'aBcDe1F2g3'", RESULTADO_ACEPTADO),
    ("'aaaaas******'", RESULTADO_TRAMPA),
    ("'HolaMundo999'", RESULTADO_ACEPTADO),
    ("'-'", RESULTADO_TRAMPA),
    ("'MeGustanLasMilanesasYElNumero73'", RESULTADO_ACEPTADO),
    (":)", RESULTADO_TRAMPA),
]

for cadena, resultado in casosString:
    assert A_String(cadena) == resultado

#################################################################

#delta Identificador
def d_ID(estado_anterior, caracter):
    if estado_anterior == 0 and caracter.isalpha():
        return 1
    if estado_anterior == 1 and caracter.isalpha():
        return 1
    if estado_anterior == 1 and caracter in digito:
        return 1

    
    return TRAMPA

#automata Identificador
def A_ID(cadena):
    Finales = [1]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_ID(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo
    
    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

casosID = [
    ("Adsga11sF", RESULTADO_ACEPTADO),    
    ("aBcDe1F2g3", RESULTADO_ACEPTADO),
    ("aaaaas******", RESULTADO_TRAMPA),
    ("999HolaMundo999", RESULTADO_TRAMPA),
    ("'-'", RESULTADO_TRAMPA),
    ("MeGustanLasMilanesasYElNumero73", RESULTADO_ACEPTADO),
    ("1S1", RESULTADO_TRAMPA),
]

for cadena, resultado in casosID:
    assert A_ID(cadena) == resultado

####################GRAMATICA SINTACTICA#####################

#delta while
def d_While(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "w":
        return 1
    if estado_anterior == 1 and caracter == "h":
        return 2
    if estado_anterior == 2 and caracter == "i":
        return 3
    if estado_anterior == 3 and caracter == "l":
        return 4
    if estado_anterior == 4 and caracter == "e":
        return 5

    
    return TRAMPA

#automata While
def A_While(cadena):
    Finales = [5]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_While(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo
    
    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

casosWhile = [
    ("while", RESULTADO_ACEPTADO),
    ("2.69a8", RESULTADO_TRAMPA),
    ("whi", RESULTADO_NO_ACEPTADO),
]

for cadena, resultado in casosWhile:
    assert A_While(cadena) == resultado

#################################################################

#delta {
def d_LlaveAbierta(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "{":
        return 1

    return TRAMPA

#automata {
def A_LlaveAbierta(cadena):
    Finales = [1]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_LlaveAbierta(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo
    
    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

casosLlaveAbierta = [
    ("{", RESULTADO_ACEPTADO),
    ("}", RESULTADO_TRAMPA),
]

#for cadena, resultado in casosCorcheteAbierto:
#    assert A_CorcheteAbierto(cadena) == resultado

#################################################################

#delta }
def d_LlaveCerrada(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "}":
        return 1

    
    return TRAMPA

#automata }
def A_LlaveCerrada(cadena):
    Finales = [1]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_LlaveCerrada(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo
    
    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

casosLlaveCerrada = [
    ("}", RESULTADO_ACEPTADO),
    ("{", RESULTADO_TRAMPA),
]

#for cadena, resultado in casosCorcheteCerrado:
#    assert A_CorcheteCerrado(cadena) == resultado

#################################################################

#delta OR
def d_OR(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "o":
        return 1
    if estado_anterior == 1 and caracter == "r":
        return 2

    
    return TRAMPA

#automata OR
def A_OR(cadena):
    Finales = [2]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_OR(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo
    
    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

casosOR = [
    ("or", RESULTADO_ACEPTADO),
    ("trampa", RESULTADO_TRAMPA),
    ("o", RESULTADO_NO_ACEPTADO),
]

for cadena, resultado in casosOR:
    assert A_OR(cadena) == resultado

#################################################################

#delta AND
def d_AND(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "a":
        return 1
    if estado_anterior == 1 and caracter == "n":
        return 2
    if estado_anterior == 2 and caracter == "d":
        return 3

    
    return TRAMPA

#automata AND
def A_AND(cadena):
    Finales = [3]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_AND(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo
    
    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

casosAND = [
    ("and", RESULTADO_ACEPTADO),
    ("trampa", RESULTADO_TRAMPA),
    ("an", RESULTADO_NO_ACEPTADO),
]

for cadena, resultado in casosAND:
    assert A_AND(cadena) == resultado

#################################################################

#delta ==
def d_DobleIgual(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "=":
        return 1
    if estado_anterior == 1 and caracter == "=":
        return 2

    
    return TRAMPA

#automata ==
def A_DobleIgual(cadena):
    Finales = [2]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_DobleIgual(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo
    
    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

casosDobleIgual = [
    ("==", RESULTADO_ACEPTADO),
    ("trampa", RESULTADO_TRAMPA),
    ("=", RESULTADO_NO_ACEPTADO),
]

for cadena, resultado in casosDobleIgual:
    assert A_DobleIgual(cadena) == resultado

#################################################################

#delta !=
def d_ExclamacionIgual(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "!":
        return 1
    if estado_anterior == 1 and caracter == "=":
        return 2

    
    return TRAMPA

#automata !=
def A_ExclamacionIgual(cadena):
    Finales = [2]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_ExclamacionIgual(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo
    
    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

casosExclamacionIgual = [
    ("!=", RESULTADO_ACEPTADO),
    ("trampa", RESULTADO_TRAMPA),
    ("!", RESULTADO_NO_ACEPTADO),
]

for cadena, resultado in casosExclamacionIgual:
    assert A_ExclamacionIgual(cadena) == resultado

#################################################################

#delta >
def d_Mayor(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == ">":
        return 1

    
    return TRAMPA

#automata >
def A_Mayor(cadena):
    Finales = [1]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_Mayor(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo
    
    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

casosMayor = [
    (">", RESULTADO_ACEPTADO),
    ("trampa", RESULTADO_TRAMPA),
]

for cadena, resultado in casosMayor:
    assert A_Mayor(cadena) == resultado

#################################################################

#delta '
def d_Apostrofo(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "'":
        return 1

    return TRAMPA

#automata '

def A_Apostrofo(cadena):
    Finales = [1]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_Apostrofo(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo

    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

casosApostrofo = [
    ("'", RESULTADO_ACEPTADO),
    ("trampa", RESULTADO_TRAMPA),
]

for cadena, resultado in casosApostrofo:
    assert A_Apostrofo(cadena) == resultado


#################################################################

#delta *
def d_Asterisco(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "*":
        return 1

    return TRAMPA

#automata *

def A_Asterisco(cadena):
    Finales = [1]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_Asterisco(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo

    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

#################################################################

#delta !
def d_Exclamacion(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "!":
        return 1

    return TRAMPA

#automata !

def A_Exclamacion(cadena):
    Finales = [1]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_Exclamacion(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo

    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

#################################################################

#delta false
def d_False(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "f":
        return 1
    if estado_anterior == 1 and caracter == "a":
        return 2
    if estado_anterior == 2 and caracter == "l":
        return 3
    if estado_anterior == 3 and caracter == "s":
        return 4
    if estado_anterior == 4 and caracter == "e":
        return 5

    return TRAMPA

#automata false

def A_False(cadena):
    Finales = [5]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_False(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo

    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO


#################################################################

#delta -
def d_Guionmedio(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "-":
        return 1

    return TRAMPA

#automata -

def A_Guionmedio(cadena):
    Finales = [1]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_Guionmedio(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo

    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

#################################################################

#delta +
def d_Mas(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "+":
        return 1

    return TRAMPA

#automata +

def A_Mas(cadena):
    Finales = [1]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_Mas(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo

    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

#################################################################

#delta <
def d_Menor(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "<":
        return 1

    return TRAMPA

#automata <

def A_Menor(cadena):
    Finales = [1]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_Menor(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo

    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

#################################################################

#delta >=
def d_Mayorigual(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == ">":
        return 1
    if estado_anterior == 1 and caracter == "=":
        return 2

    return TRAMPA

#automata >=

def A_Mayorigual(cadena):
    Finales = [2]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_Mayorigual(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo

    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

#################################################################

#delta <=
def d_Menorigual(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "<":
        return 1
    if estado_anterior == 1 and caracter == "=":
        return 2

    return TRAMPA

#automata <=

def A_Menorigual(cadena):
    Finales = [2]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_Menorigual(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo

    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

#################################################################

#delta .
def d_Punto(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == ".":
        return 1

    return TRAMPA

#automata .

def A_Punto(cadena):
    Finales = [1]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_Punto(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo

    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

#################################################################

#delta /
def d_Slash(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "/":
        return 1

    return TRAMPA

#automata /

def A_Slash(cadena):
    Finales = [1]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_Slash(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo

    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

#################################################################

#delta true
def d_True(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "t":
        return 1
    if estado_anterior == 1 and caracter == "r":
        return 2
    if estado_anterior == 2 and caracter == "u":
        return 3
    if estado_anterior == 3 and caracter == "e":
        return 4

    return TRAMPA

#automata true

def A_True(cadena):
    Finales = [4]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_True(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo

    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

#################################################################

#delta eof
def d_EOF(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "e":
        return 1
    if estado_anterior == 1 and caracter == "o":
        return 2
    if estado_anterior == 2 and caracter == "f":
        return 3

    
    return TRAMPA

#automata eof

def A_EOF(cadena):
    Finales = [3]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_EOF(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo

    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO


#################################################################

#delta fun
def d_FUN(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "f":
        return 1
    if estado_anterior == 1 and caracter == "u":
        return 2
    if estado_anterior == 2 and caracter == "n":
        return 3

    
    return TRAMPA

#automata fun

def A_FUN(cadena):
    Finales = [3]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_FUN(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo

    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

#################################################################

#delta (
def d_ParenOpen(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "(":
        return 1

    return TRAMPA

#automata (

def A_ParenOpen(cadena):
    Finales = [1]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_ParenOpen(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo

    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

#################################################################

#delta )
def d_ParenClose(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == ")":
        return 1

    return TRAMPA

#automata )

def A_ParenClose(cadena):
    Finales = [1]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_ParenClose(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo

    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

#################################################################

#delta ,
def d_Coma(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == ",":
        return 1

    return TRAMPA

#automata ,

def A_Coma(cadena):
    Finales = [1]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_Coma(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo

    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

#################################################################

#delta ;
def d_PuntoComa(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == ";":
        return 1

    return TRAMPA

#automata ;

def A_PuntoComa(cadena):
    Finales = [1]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_PuntoComa(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo

    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

#################################################################

#delta var
def d_VAR(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "v":
        return 1
    if estado_anterior == 1 and caracter == "a":
        return 2
    if estado_anterior == 2 and caracter == "r":
        return 3
    
    return TRAMPA

#automata var

def A_VAR(cadena):
    Finales = [3]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_VAR(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo

    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

#################################################################

#delta for
def d_FOR(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "f":
        return 1
    if estado_anterior == 1 and caracter == "o":
        return 2
    if estado_anterior == 2 and caracter == "r":
        return 3
    
    return TRAMPA

#automata for

def A_FOR(cadena):
    Finales = [3]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_FOR(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo

    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

#################################################################

#delta =
def d_Igual(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "=":
        return 1

    return TRAMPA

#automata =

def A_Igual(cadena):
    Finales = [1]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_Igual(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo

    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

#################################################################

#delta else
def d_Else(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "e":
        return 1
    if estado_anterior == 1 and caracter == "l":
        return 2
    if estado_anterior == 2 and caracter == "s":
        return 3
    if estado_anterior == 3 and caracter == "e":
        return 4

    return TRAMPA

#automata else

def A_Else(cadena):
    Finales = [4]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_Else(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo

    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

#################################################################

#delta if
def d_If(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "i":
        return 1
    if estado_anterior == 1 and caracter == "f":
        return 2

    return TRAMPA

#automata if

def A_If(cadena):
    Finales = [2]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_If(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo

    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

#################################################################

#delta return
def d_Return(estado_anterior, caracter):
    if estado_anterior == 0 and caracter == "r":
        return 1
    if estado_anterior == 1 and caracter == "e":
        return 2
    if estado_anterior == 2 and caracter == "t":
        return 3
    if estado_anterior == 3 and caracter == "u":
        return 4
    if estado_anterior == 4 and caracter == "r":
        return 5
    if estado_anterior == 5 and caracter == "n":
        return 6

    return TRAMPA

#automata return

def A_Return(cadena):
    Finales = [6]
    estado_actual = 0

    for caracter in cadena:
        estado_proximo = d_Return(estado_actual, caracter)
        if estado_proximo == TRAMPA:
            return RESULTADO_TRAMPA
        estado_actual = estado_proximo

    if estado_actual in Finales:
        return RESULTADO_ACEPTADO
    else:
        return RESULTADO_NO_ACEPTADO

cadena = "999"
