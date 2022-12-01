#Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print('Valores sorteados: ', end='')
for n in num:
    print(n, end=' ')

print(f'\nO maior número dentre os sorteados é {max(num)}')
print(f'O menor número dentre os sorteados é {min(num)}')