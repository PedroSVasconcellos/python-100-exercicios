# Exercício Python 028:
# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

numPC = randint(0, 5)

print('-=-' * 20)
print('Vou pensar num número de 0 a 5, tente adivinhar qual é!')
print('-=-' * 20)
chute = int(input('Que número eu pensei? '))
print('PROCESSANDO...')
sleep(1)

if chute == numPC:
    print('Parabéns!!! Você acertou!')
else:
    print(f'Errou o chute, eu pensei em {numPC} tente novamente.')
