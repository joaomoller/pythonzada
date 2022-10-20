'''
iniciar com letra, pode conter números, separar _, letras minúsculas
'''
nome = 'Joao'
idade = 23
altura = 1.81
e_maior = idade > 18
peso = 85
imc = peso / altura ** 2

print('Nome: ', nome)
print('Idade: ', idade)
print('Altura: ', altura)
print('É maior: ', e_maior)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)