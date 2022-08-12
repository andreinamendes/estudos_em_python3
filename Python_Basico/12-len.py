usuario = input('Digite o seu usuário: ')
quantidade = len(usuario)

print(f'A quantidade de caracteres é {quantidade} e o tipo do valor passado é: {type(quantidade)}')

print(quantidade, usuario.__len__())