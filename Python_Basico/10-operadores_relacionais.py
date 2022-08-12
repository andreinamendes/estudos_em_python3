"""
Operadores relacionais
  - Igualdade      |   ==
  - Maior que      |   >
  - Maior ou igual |   >=
  - Menor          |   <
  - Menor ou igual |   <=
  - Diferente      |   !=
  
  -> Irão retornar valores booleanos entre quaisquer elementos
  -> Sua precedência é definida pela ordem de criação ou por ()
"""

print(2 == 2)

if 50 < 100:
  print('Menor')
elif 50 > 100:
  print('Maior')
else:
  print('Igual')