"""
Operadores lógicos
  -> São usados para realizar comparações
  
  - Conjunção     | and
  - Disjunção     | or
  - Negação       | not
  - Pertence      | in
  - Não pertence  | not in
  
"""

if type(2) == int and type('A') == int:
    print('Tudo certo')
else:
    print('Algo está errado')

if type(2) == int or type('A') == int:
    print('Algo está certo')
else:
    print('Tudo errado')

x = True
x = not True
print(x)

nome = 'Andreina'

if 'a' in nome:
    print('O nome contém "a"')
elif 'a' not in nome:
    print('O nome não contém "a"')