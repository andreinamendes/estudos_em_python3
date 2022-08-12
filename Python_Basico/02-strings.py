"""
String
 - É um tipo composto de dados.
 - Pode ser representado por '' ou "".
 - Pode ser qualquer valor que seja representado entre aspas.
 - Pode ser iterado.
 - Se definir uma string com um tipo de aspas específicas e na metade da instanciação, utilizar as mesmas aspas ele vai considerar que as aspas fazem parte da string.
 - Se definir uma string com um tipo de aspas específicas e na metade da instanciação, e utilizar as mesmas aspas em algum momento da string o interpretador vai considerar como o fim da string e a continuação da mesma não vai ser entendida como parte, o que provalmente vai causar um erro.
"""

print('Isto é uma String')
print('Isto também "é uma" string')
print('Isto também \'é uma\' string') # Código feio que só

print("Isto também é uma string")
print("Isto também 'é uma' string")
print("Isto também \"é uma\" string") # Código feio que só

print("Isto também é uma string com quebra de linha ao final.\n")
print("Isto também é uma string\n com quebra de linha no meio.")
print(r"Isto também é uma string\n com comandos de quebra de linha no meio que não será interpretado por conta do r no começo.") # O r ignora quaiquer comandos dento da string, não é recomendado o uso