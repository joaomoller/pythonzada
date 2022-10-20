'''
Tipos de dados
str - string - textos 'assim' "assim"
int - inteiro - 123456 0 -10 -20 -50 -60 -15000 1500
float - real/ponto flutuante - 10.50 1.5 -10.10 -50.93 0.0
bool - booleano/lógico - True/False 10 == 10 'L' == 'L'
'''
print('Joao', type('Joao'))
print(10, type(10))
print(24.69, type(24.69))
print('X' == 'Y', type('X' == 'Y'))

print('Joao', type('Joao'), bool('Joao'))

# string: Nome
print('Joao Vitor Moller', type('Joao Vitor Moller'))

# Idade: int
print(23, type(23))

# Altura: float
print(1.82, type(1.82))

# É maior de idade x > 18
print(23 > 18, type(23 > 18))