"""
CPF = 168.995.350-09
------------------------------------------------
1 * 10 = 10           #    1 * 11 = 11 <-
6 * 9  = 54           #    6 * 10 = 60
8 * 8  = 64           #    8 *  9 = 72
9 * 7  = 63           #    9 *  8 = 72
9 * 6  = 54           #    9 *  7 = 63
5 * 5  = 25           #    5 *  6 = 30
3 * 4  = 12           #    3 *  5 = 15
5 * 3  = 15           #    5 *  4 = 20
0 * 2  = 0            #    0 *  3 = 0
                      # -> 0 *  2 = 0
         297          #             343
11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
11 > 9 = 0            #
Digito 1 = 0          #   Digito 2 = 9
"""

def calcular(x, cpf):
  sum = 0
  
  for value in cpf:
    if value.isnumeric():
      #print(f'{value} * {x} = {int(value) * x}')
      sum += int(value) * x
      x -= 1
  
  return 0 if 11 - (sum % 11) > 9 else 11 - (sum % 11)
  
if __name__ == '__main__':
  cpf = input("Digite o seu cpf: ")
  
  digito1 = calcular(10, cpf[0:9])
  novo_cpf = cpf[0:9] + str(digito1)
  digito2 = calcular(11, novo_cpf)
  novo_cpf += str(digito2)
  
  print('CPF Válido!' if novo_cpf == cpf else 'CPF Inválido!')