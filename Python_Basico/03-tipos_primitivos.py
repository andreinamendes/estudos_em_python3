"""
Tipos primitivos
 - String - str
 - Inteiro - int
    -> Se for instanciado utilizando aspas, será considerado como um valor do tipo string e não inteiro
 - Ponto flutuante ou real - float
    -> Deve ser representado com . como em 10.5 ou 25.0
 - Valor lógico - bool
"""

print('Andreina', type('Andreina')) # Classe type, retorna o tipo do valor passado como parâmetro
print(10, type(10))
print(0, type(0))
print(2.5, type(2.5))
print(0.0, type(0.0))
print(True, type(True))
print(10 == 5, type(10 == 5))
print('L' == 'L', type('L' == 'L'))