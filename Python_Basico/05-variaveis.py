"""
Variáveis
  - São formas de salvar valores na memória do computador.
  - O python é considerado uma linguagem de tipagem dinâmica, ou seja, na definição de variáveis não é necessária a tipagem das mesmas como int a ou float b, apenas colocando o nome e o valor da variável que será utilizado para definir o tipo.
  - Podem ter seu valor alterado para qualquer tipo no decorrer da execução do código.
"""

nome = str() # Variáveis podem ser instanciadas com a definição do próprio tipo

nome = 'Andreina' # Definição de variável do tipo string sem determinar tipo no início e já instanciando com o valor.
idade = 22
altura = 1.67
e_maior = idade > 18

print('Nome: ', nome)
print('idade: ', idade)
print('altura: ', altura)
print('É maior de idade?', e_maior)