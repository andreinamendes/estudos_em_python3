"""
O python descreve formas para pular determinados bloos de código e este não ficar com erro caso o código real não tenha sido digitado ainda.
  - pass
  - ...
"""

valor = True

if valor:
  pass
else:
  print('Tchau')
  
if valor:
  ...
else:
  print('Tchau')