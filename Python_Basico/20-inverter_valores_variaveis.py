"""
A inversão de valores em python pode ser feita de maneira bem mais simples que em outras linguagens.
"""

x = 10
y = 'Luiz'

print(f'X = {x} | Y = {y}')

x, y = y, x

print(f'X = {x} | Y = {y}')

z = 'Andreina'

x, y, z = z, x, y

print(f'X = {x} | Y = {y} | Z = {z}')