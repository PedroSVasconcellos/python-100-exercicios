# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

jogo = []
temp = []
cont = 0

print('-' * 30)
print(f"{'MEGA SENA':^30}")
print('-' * 30)
j = int(input('Quantos jogos você quer sortear? '))

for i in range(0, j):
    for c in range(0, 6):
        ran = randint(0, 60)
        while True:
            if ran not in temp:
                temp.append(ran)
                break
            else:
                ran = randint(0, 60)
    sleep(0.75)
    temp.sort()
    jogo.append(temp[:])
    cont += 1
    print(f'Jogo {cont} {temp}')
    temp.clear()
