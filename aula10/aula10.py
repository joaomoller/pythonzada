'''
operadores relacionais
== igualdade
> maior que
>= maior ou igual a
< menor que
<= menor ou igual a
 != diferente
'''

nome = input('qual o seu nome? ')
idade = input('qual a sua idade? ')
idade = int(idade)

idade_menor = 18
idade_maior = 30

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pehgar o emprestimo')
else:
    print(f'{nome} NÃO pode pegar o emprestimo')