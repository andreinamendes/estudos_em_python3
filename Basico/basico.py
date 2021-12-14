# Esta é a sintaxe para estabelecer um comentário em uma linha

print("Hello World") # Isto é um comentário em uma mesma linha que há código

"""
print("1")
print("2")
print("3")
print("4")
print("5")

Isto é um comentário multilinha com aspas duplas
"""

'''
Isso é um comentário multilinha com aspas simples
'''

print("Andreina") # Saída: Andreina
print("Andreina Mendes") # Saída: Andreina Mendes
print("Andreina", "Mendes") # Saída: AndreinaMendes
print("Andreina", "Mendes", sep=' ') # Saída: Andreina Mendes
print("Andreina", "Mendes", sep=' ', end=' ') # Andreina Mendes (Com um espaço no final)
# O padrão de end é \n (Quebra de linha)

# Gerar o CPF 824.176.070-18 com print

print("824", "176", "070", sep='.', end='-18')

# ou

print("824", "176", "070", sep='.', end='-')
print("18")

