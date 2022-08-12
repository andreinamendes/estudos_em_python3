"""
  Split - Divide listas e strings
  Join - Une elementos de uma lista de strings em uma string apenas
  Enumerate - Faz a numeração de elementos de uma lista ou string e retorna uma tupla com esses valores
"""

import string

string = "O Brasil é o país do futebol, o Brasil é penta."
lista1 = string.split(' ')
lista2 = string.split(',')

print(f'A lista1 é: {lista1}.')
print(f'A lista2 é: {lista2}.')

print('\n')

for valor in lista1: # iterando sobre a lista
  print(f'A palavra {valor} apareceu {lista1.count(valor)} na frase.') # Contando os elementos da lista individualmente
  
print('\n')

print(f"A nova lista1 é: {' '.join(lista1)}")
print(f"A nova lista2 é: {'.'.join(lista2)}")

for index, valor in enumerate(string):
  print(f'O índice do {valor} é {index}.')