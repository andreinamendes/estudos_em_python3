nome = 'Andreina'
sobrenome = 'Mendes'

nome_formatado = '{n:#>50} {s:#<50}'.format(n = nome, s = sobrenome)

print(nome_formatado)