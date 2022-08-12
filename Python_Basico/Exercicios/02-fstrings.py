"""
Mostrar os dados do cálculo de IMC com fstrings
"""

nome = 'Andreina'
idade = 22
altura = 1.67
e_maior = idade > 18
peso = 62.0
ano_atual = 2022
ano_nasc = ano_atual - idade

imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos e {altura} de altura.') # Usando fstrings
print(f'{nome} pesa {peso} e seu imc é de {imc:.2f}.')
print(f'{nome} nasceu em {ano_nasc}.')