nome = 'Andreina'
idade = 21
altura = 1.64
peso = 58.0
ano = 2021
ano_nasc = ano - idade
imc = peso / (altura**altura)

print(f'{nome} nasceu em {ano_nasc} e estamos no ano de {ano}, logo tem {idade} anos de idade, seu peso e de {peso} e altura {altura}, logo o seu IMC sera de {imc:.2f}.')