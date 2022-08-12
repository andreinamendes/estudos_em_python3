"""
Listas são formas de armazenar valores de quailquer tipos de forma que possamos iterar sobre eles e assim relaizar inúmeras manipulações. Exemplo:
  lista = [1, 2, 3, 4, 'a', 'b', 'c', 10.5, 13]
"""

lista = list()

lista1 = [1, 2, 3, 4, 'a', 'b', 'c', 10.5, 13]
print(lista1[::2]) # Faz fatiamento de listas da mesma forma com strings

lista2 = [1, 2, 3]
lista3 = [4, 5, 6]
lista4 = [7, 8, 9]
print(f'Listas 2, 3 e 4 concatenadas: {lista2 + lista3 + lista4}') # Concatena listas para mostrar os dados}

lista2.extend(lista3) # Adiciona uma list ao final da outra
print(f'Nova lista2: {lista2}')

lista4.append(10) # Adiciona um valor ao fim da lista
print(f'Nova lista4: {lista4}')

lista2.insert(0, 0) # Adiciona valores em uma posição específica
print(f'Nova lista2: {lista2}')

lista4.pop() # Remove o último elemento da lista
print(f'Nova lista4: {lista4}')

print(f'Listas 2, 3 e 4 atualizadas e concatenadas: {lista2 + lista4}')

del(lista1[4::2]) # Remove um determinado escopo de elementos utilizando fatiamento
print(f'Nova lista1: {lista1}')

lista5 = list(range(1, 10, 2)) # Cria uma lista utilizando o retorno da função range realizando um casting para o tipo de valor list
print(f'Lista5: {lista5}')