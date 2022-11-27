# Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

mulheresMenos20 = homens = maiores = total = 0

while True:
    idade = int(input('Qual a idade? '))
    if idade >= 18:
        maiores += 1
    sexo = ' '
    while sexo not in 'mf':
        sexo = str(input('Qual o sexo? [M/F] ')).strip().lower()[0]
    if sexo == 'm':
        homens += 1
    if sexo == 'f' and idade < 20:
        mulheresMenos20 += 1
    total += 1
    continuar = ' '
    while continuar not in 'sn':
        continuar = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if continuar in 'Ss':
        print('=' * 20)
    if continuar in 'Nn':
        break

print('=' * 20)
print(f'Foram cadastradas {total} pessoas.')
print(f'Existem {maiores} maiores de 18 anos.')
print(f'{homens} homens cadastrados.')
print(f'E {mulheresMenos20} mulheres com menos de 20 anos.')