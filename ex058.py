# Exercício Python 058:
# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Consegue adivinhar qual foi?')
ncomp = randint(0, 10)
c = 0
acertou = False
while not acertou:
    n = int(input('Qual seu palpite? '))
    c += 1
    if n == ncomp:
        acertou = True
    elif n < ncomp:
        print('Mais alto!')
    elif n > ncomp:
        print('Mais baixo!')

print(f'Parabéns, você acertou. Foram {c} tentativas.')


