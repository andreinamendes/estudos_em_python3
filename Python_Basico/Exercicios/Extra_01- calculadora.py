"""
Fazer uma calculadora completa que utilize apenas o laço while
"""

def pegar_op():
  ops = ['+', '-', '/', '%', '//', '*', '**']
  while True:
    aux = input('Digite a operação: ')
    if aux in ops:
      return str(aux)
    else:
      print("O parâmetro digitado é inválido.")
      
def pegar_qtd_valores():
  while True:
    aux = input('Digite a quantidade de valores da operação: ')
    if aux.isnumeric():
      return int(aux)
    else:
      print("O parâmetro digitado é inválido.")
  
def pegar_valores(qtd):
  i = 0
  aux = [int()]*qtd
  
  while i < qtd:
    value = input(f'Digite o valor {i + 1}: ')
    if value.isnumeric():
      aux[i] = int(value)
      i += 1
    else:
      print("O parâmetro digitado é inválido, digite novamente.")
      
  return aux

def realizarop(qtd, op, valores):
  result = int()
  
  match op:
    case '+':
      a = 0
      result = 0
      while a < len(valores):
        result += valores[a]
        a += 1
    case '-':
      a = 1
      result = valores[0]
      while a < len(valores):
        result -= valores[a]
        a += 1
    case '*':
      a = 0
      result = 1
      while a < len(valores):
        result *= valores[a]
        a += 1
    case '/':
      a = 1
      result = valores[0]
      while a < len(valores):
        result /= valores[a]
        a += 1
    case '//':
      a = 1
      result = valores[0]
      while a < len(valores):
        result //= valores[a]
        a += 1
    case '**':
      a = 1
      result = valores[0]
      while a < len(valores):
        result **= valores[a]
        a += 1
    case '%':
      a = 1
      result = valores[0]
      while a < len(valores):
        result %= valores[a]
        a += 1
        
  return result

if __name__ == '__main__':
  op = pegar_op()
  qtd = pegar_qtd_valores()
  valores = pegar_valores(qtd)
  print(f'O resultado da operação de {op} entre os valores {valores} é: {realizarop(qtd, op, valores)}.')