"""
Operadores Condicionais
  - O Python implementa a forma básica de realizar operações condicionais, o if e o else.
  - No caso de testar novamente uma outra condição dentro da estrutura, o python devine como elif, o se não se.
"""

if 10 == 12:
  print('Verdadeiro')
else:
  print('Falso')
  
if 10 > 12:
  print('Maior')
elif 10 < 12:
  print('Menor')
else:
  print('Igual')