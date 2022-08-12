"""
O operador ternário permite, enas linguagens nas quais é implementado, a simplificação de operações condicionais.
"""

# Sem operador ternário

logged_user = False

if logged_user:
  msg = 'Usuário logado!'
else:
  msg = 'Usuário precisa fazer login.'
  
print(msg)

# Com operador ternário

logged_user = True

msg = 'Usuário logado!' if logged_user else 'Usuário precisa fazer login.'

print(msg)