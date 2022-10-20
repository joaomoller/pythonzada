'''
entrada de dados
'''
nome = input('qual o seu nome? ')
idade = input('qual a sua idade? ')

ano_nascimento = 2022 - int(idade)


print()
print(f'{nome} tem {idade} anos e nasceu em {ano_nascimento}')
print()

numero1 = int(input('digite um numero: '))
numero2 = input('digite outro numero: ')
numero2 = int(numero2)

print(numero1 + numero2)