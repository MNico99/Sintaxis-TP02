from lex import *
from parser import *

casosLexer = [
    (
        "if ( a >= b then *",  #Cadena a evaluar
        [('IF', 'if'), ('PAREN_OPEN','('), ('ID', 'a'), ('MAYOR_IGUAL', '>='), ('ID', 'b'), ('ID', 'then'), ('ASTERISCO', '*'), ('EOF', 'EOF')] #Tokens esperados
     ),

    (
        "if while variable fun", 
        [('IF', 'if'), ('WHILE', 'while'), ('ID', 'variable'), ('FUN', 'fun'), ('EOF', 'EOF')]
    ),

    (
        "while ( a + b == c ) then", 
        [('WHILE', 'while'), ('PAREN_OPEN', '('), ('ID', 'a'), ('MAS', '+'), ('ID', 'b'), ('DOBLE_IGUAL', '=='), ('ID', 'c'), ('PAREN_CLOSE', ')'), ('ID', 'then'), ('EOF', 'EOF')]
    ),

    (
        "palabra = 'palabra'", 
        [('ID', 'palabra'), ('IGUAL', '='), ('STRING', "'palabra'"), ('EOF', 'EOF')]
    ),

    (
        "while eof ! else variable",
        [('WHILE', 'while'), ('EOF', 'eof'), ('EXCLAMACION', '!'), ('ELSE', 'else'), ('ID', 'variable'), ('EOF', 'EOF')]
    ),

    (
        "if ( a + b = x ) and ( a + x = c )", 
        [('IF', 'if'), ('PAREN_OPEN', '('), ('ID', 'a'), ('MAS', '+'), ('ID', 'b'), ('IGUAL', '='), ('ID', 'x'), ('PAREN_CLOSE', ')'), ('AND', 'and'), ('PAREN_OPEN', '('), ('ID', 'a'), ('MAS', '+'), ('ID', 'x'), ('IGUAL', '='), ('ID', 'c'), ('PAREN_CLOSE', ')'), ('EOF', 'EOF')]
    ),

    (
        "var vector = ( 1 , casa ) , ( 2 , pepe )",
        [('VAR', 'var'), ('ID', 'vector'), ('IGUAL', '='), ('PAREN_OPEN', '('), ('NUM', '1'), ('COMA', ','), ('ID', 'casa'), ('PAREN_CLOSE', ')'), ('COMA', ','), ('PAREN_OPEN', '('), ('NUM', '2'), ('COMA', ','), ('ID', 'pepe'), ('PAREN_CLOSE', ')'), ('EOF', 'EOF')]
    ),

    (
        "var casa = 'casaDeAldo'", 
        [('VAR', 'var'), ('ID', 'casa'), ('IGUAL', '='), ('STRING', "'casaDeAldo'"), ('EOF', 'EOF')]
    ),

    (
        "vector { 2 } = 32",
        [('ID', 'vector'), ('LLAVE_ABIERTA', '{'), ('NUM', '2'), ('LLAVE_CERRADA', '}'), ('IGUAL', '='), ('NUM', '32'), ('EOF', 'EOF')]
    ),

    (
        "var b - a - c = 15",
        [('VAR', 'var'), ('ID', 'b'), ('GUION_MEDIO', '-'), ('ID', 'a'), ('GUION_MEDIO', '-'), ('ID', 'c'), ('IGUAL', '='), ('NUM', '15'), ('EOF', 'EOF')]
    ),

    (
        "if ( a = b ) and c = 15 then",
        [('IF', 'if'), ('PAREN_OPEN', '('), ('ID', 'a'), ('IGUAL', '='), ('ID', 'b'), ('PAREN_CLOSE', ')'), ('AND', 'and'), ('ID', 'c'), ('IGUAL', '='), ('NUM', '15'), ('ID', 'then'), ('EOF', 'EOF')]
    ),

    (
        "skere = 'sk' + 'ere'", 
        [('ID', 'skere'), ('IGUAL', '='), ('STRING', "'sk'"), ('MAS', '+'), ('STRING', "'ere'"), ('EOF', 'EOF')]
    ),

    (
        "while ( b = c ) or ( a = c )", 
        [('WHILE', 'while'), ('PAREN_OPEN', '('), ('ID', 'b'), ('IGUAL', '='), ('ID', 'c'), ('PAREN_CLOSE', ')'), ('OR', 'or'), ('PAREN_OPEN', '('), ('ID', 'a'), ('IGUAL', '='), ('ID', 'c'), ('PAREN_CLOSE', ')'), ('EOF', 'EOF')]
    ),

    (
        "1 + 2 + 3 + 4 = 11", 
        [('NUM', '1'), ('MAS', '+'), ('NUM', '2'), ('MAS', '+'), ('NUM', '3'), ('MAS', '+'), ('NUM', '4'), ('IGUAL', '='), ('NUM', '11'), ('EOF', 'EOF')]
    ),

    (
        "'casa' + 'aldo' = 'casaDeAldo'", 
        [('STRING', "'casa'"), ('MAS', '+'), ('STRING', "'aldo'"), ('IGUAL', '='), ('STRING', "'casaDeAldo'"), ('EOF', 'EOF')]
    ) 
]

for cadena, resultado in casosLexer:
    assert lex(cadena) == resultado

