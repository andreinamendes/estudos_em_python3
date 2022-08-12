"""
A função para entrada de dados em Python é input(), esta função sempre salva os valores passados no terminal no formato de string.
"""

nome = input('Qual o seu nome? ' ) # Forma básica de uso
print(f'O valor passado foi {nome} e o tipo da variável é {type(nome)}.') 
idade = input('Qual a sua idade? ')
print(f'O valor passado foi {idade} e o tipo da variável é {type(idade)}.')
idade = int(input('Qual a sua idade? ')) # Recebendo o dado e já fazendo o casting
print(f'O valor passado foi {idade} e o tipo da variável é {type(idade)}.')