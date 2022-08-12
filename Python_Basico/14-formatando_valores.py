"""
Formatando valores com modificadores
  - Texto(strings)                        |  :s
  - Inteiros(int)                         |  :d
  - Números de ponto flutuante(float)     |  :f
  - Quantidade de cadas decimais(float)   |  :.(qtd_casas)f
  - :(Caractere)(> ou < ou ^)(Quantidade)(Tipo - s, d ou f)
  
  > - Esquerda
  < - Direita
  ^ - Centro  
"""

valor = 23.234234234
print(f'{valor:.2f}') # Imprimir um valor float com 2 casas

num_1 = 1
print(f'{num_1:.10f}') # Imprimir um valor com 10 casas decimais, mesmo não sendo float
print(f'{num_1:0>10}') # Imprimir um valor com 10 casas decimais a esquerda

num_2 = 1150
print(f'{num_2:0<10f}') # Imprimir um valor com 10 casas decimais a direita, mesmo não sendo float
print(f'{num_2:.2f}')

nome = 'Andreina'
print(f'{nome:@^50}') # Printando diversos @ com o nome no meio definido por ^ com todos os caracteres somando 50
print(nome.lower()) # Mostra todos os valores minúsculos
print(nome.upper()) # Mostra todos os valores maiúsculos
print(nome.title()) # Coloca a primeira letra de cada nome como maiúscula

novo_nome = '{n:0^20}'.format(n=nome) # Associando operadores de formatação com a função .format()
print(novo_nome)