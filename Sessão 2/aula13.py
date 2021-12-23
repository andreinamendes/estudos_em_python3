print("Andreina") # Saída: Andreina
print("Andreina Mendes") # Saída: Andreina Mendes
print("Andreina", "Mendes") # Saída: AndreinaMendes
print("Andreina", "Mendes", sep=' ') # Saída: Andreina Mendes
print("Andreina", "Mendes", sep=' ', end=' ') # Andreina Mendes (Com um espaço no final)
# O padrão de end é \n (Quebra de linha)

# Gerar o CPF 824.176.070-18 com print

print("824", "176", "070", sep='.', end='-18')

# ou

print("824", "176", "070", sep='.', end='-')
print("18")