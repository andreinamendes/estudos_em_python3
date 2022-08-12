"""
Fazer um único laço que print valores da seguinte forma:
0 10
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2
"""

for x, y in enumerate(list(range(10, 1, -1))):
  print(f'X = {x} | Y = {y}')