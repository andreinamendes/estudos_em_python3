"""
Realizar o cálculo de IMC e mostrar os dados
"""

nome = 'Andreina'
idade = 22
altura = 1.67
e_maior = idade > 18
peso = 80

imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos de idade, e seu imc é', imc)