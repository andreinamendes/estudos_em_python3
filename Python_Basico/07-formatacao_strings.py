"""
No python existem diversas formas de formatar strings.
  - fstrings
  - format()
"""

nome = 'Andreina'
idade = 22
altura = 1.67
e_maior = idade > 18
peso = 80

imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos de idade, e seu imc é {imc:.2f}.') # Usando fstrings
print('{} tem {} de idade, e seu imc é {:.2f}.'.format(nome, idade, imc)) # Usando a função format()
print('{1}{0}{2} tem {1} de idade, e seu imc é {2}.'.format(nome, idade, imc)) # Usando a função format() e, caso seja necessário realizar a repetição de algum valor pode ser definido dentro das chavez um valor que representa a ordem das variáveis definidas dentro da função format(), e assim poder colocar os valores dessas variáveis em qualquer ponto da string referenciando com a posição.
print('{x} tem {y} de idade, e seu imc é {z:.2f}.'.format(x=nome, y=idade, z=imc))