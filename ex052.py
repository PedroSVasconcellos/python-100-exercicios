#Exercício Python 052:
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número: '))
cont = 0

for c in range(1, n+1):
    if n % c == 0:
        cont += 1
        print(f'\033[33m{c}\033[m', end=" ")
    else:
        print(f'\033[31m{c}\033[m', end=" ")

print(f'\nO número {n} foi divisível {cont} vezes')

if cont == 2:
    print(f'O número {n} \033[32mÉ PRIMO\033[m!')
else:
    print(f'O número {n} \033[31mNÃO\033[m é primo!')

