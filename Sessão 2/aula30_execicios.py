""""Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar. Caso o usuário não digite um número inetiro, informe que não é um número inteiro."""

num1 = input("Digite um número: ")

if num1.isdigit():
  if int(num1) % 2 == 0:
    print(f"{num1} é par.")
  else:
    print(f"{num1} é ímpar.")
else:
  print(f"{num1} não é um número.")

"""Faça um programa que pergunte a hora ao usuário, baseando-se no horário descrito, exiba a saudação apropriada.
Bom dia 0-11
boa tarde 12-17
Boa noite 18-23
"""

try:
  hora = int(input("Digite a hora atual: "))
  
  if hora >= 0 and hora <= 11:
    print("Bom dia!")
  elif hora >= 12 and hora <= 17:
    print("Boa tarde!")
  else:
    print("Boa noite!")
    
except:
  print("Você não digitou um número, execute o programa novamente.")
  
"""Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 letras escreva "Seu nome é muito grande"."""

nome = input("Digite o seu nome: ")
len_nome = len(nome)

if len_nome <= 4:
  print("Seu nome é curto.")
elif len_nome >= 5 and len_nome <= 6:
  print("Seu nome é normal.")
else:
  print("Seu nome é muito grande.")