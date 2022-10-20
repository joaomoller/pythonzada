nome = 'Joao'
idade = 23
altura = 1.81
peso = 85
ano = 2022
nascimento = ano - idade
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso} kg')
print(f'O imc de {nome} é {imc:.2f}')
print(f'{nome} nasceu em {nascimento}')