nome = 'Andreina'
idade = 21
altura = 1.64
peso = 58

print(nome + " tem " + str(idade) + " anos de idade e " + str(altura) + "m de altura, alem de " + str(peso) + "kg.")
print(f"{nome} tem {idade} anos de idade e {altura}m de altura, alem de {peso}kg.")
print("{} tem {} anos de idade e {}m de altura, alem de {}kg".format(nome, idade, altura, peso))
print("{i} tem {j} anos de idade e {k}m de altura, alem de {l}kg".format(i=nome, j=idade, k=altura, l=peso))
