"""
Desenpacotamento de listas
"""

lista = ['Luiz', 'João', 1, 2, 3, 4, 5, 6]

n1, n2, n3, *outra_lista = lista # Quebra a lista entre n1, n2 e n3 e o resto coloca na variável outra_lista sendo a lista final

print(n1, n2, n3, outra_lista)

*outra_lista, n1, n2, n3 = lista # O * define a variável em seguida como parte da lista, no caso seria o começo e os três ultimos nessas variáveis n1, n2 e n3

print(n1, n2, n3, outra_lista)

*_, n1, n2, n3 = lista # Mesma coisa da linha 11 mas sem se preocupar com os valores iniciais da lista

print(n1, n2, n3, outra_lista)