'''
operadores logicos
and, or, not
in e not in
'''

usuario = input('nome de usuario: ')
senha = input('senha do usuario: ')

usuario_bd = 'joao'
senha_bd = '123'

if usuario_bd == usuario and senha_bd == senha:
    print('voce esta logado')
else:
    print('usuario ou senha invalidos')
