"""
As strings em python são uma forma de armazenamento de dados dinâmica que permite indexação e iteração, devido a isso, podemos manipulá-las de diversas formas.

Podemos ter indexações com valores positivos e negativos, exemplo:
  a = "Andreina"
  print(a[2]) => d
  print(a[-1]) => a
  
Podemos também realizar o fatiamento de strings, exemplo:
  texto = "Andreina"
  print(texto[2:-1]) => drein
  
Podemos também relalizar o fatiamento de strings e listas da seguinte forma:
  string[start:stop:step]
  string[1:2]
  string[1:4]
  string[1:4:2]
  string[::2]
"""

texto = "Andreina Mendes é uma estudante de Ciência da Computação"
print(texto[1])
print(texto[-1])

a = "Andreina"
print(a[2])
print(a[:-1])

texto = "Andreina"
print(texto[:-1])

print(len(texto))