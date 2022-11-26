#Exercício Python 057:
# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Qual o seu sexo [M/F]? ')).strip()[0]

while sexo not in 'FfMm':
    print('Caracter \033[31minválido\033[m. Digite "M" ou "F": ')
    sexo = str(input('Digite de novo: ')).strip().upper()[0]

print(f'O sexo registrado foi \033[33m{sexo.upper()}\033[m')
