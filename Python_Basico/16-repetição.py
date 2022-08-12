"""
Assim como em outras linguagens o python define estruturas de repetição, no caso temos While e for.

Nos laços while e for, podemos utilizar as palavras reservadas continue que iá pular para a próxima iteração e a palavra breack que irá finalizar o laço.

A função range é utilizada no python como forma de definir um escopo de iteração e como será feita a mesma, esta função retorna a própria função e não uma lista. A função segue a seguinte estrutura:
  range(start=0, stop, step=1)
"""

contador = 0
acumulador = 0

while contador <= 10: # While com else
  print(contador,'|', acumulador)
  
  if contador > 5:
    break
  
  acumulador += contador
  contador += 1
else:
  print('Cheguei no else.')
print('Isso será executado.')

texto = 'Python'

for letra in texto:
  print(letra, end=' ')

print('\n')

for numero in range(10):
  print(numero, end=' ')
  
print('\n')

for numero in range(20, 10, -1):
  print(numero, end=' ')
  
for n in range(100):
  if n % 8 ==0:
    print(n, end=' ')