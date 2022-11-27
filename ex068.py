# Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
cont = 0
while True:
    jog = int(input('Jogue um número: '))
    pc = randint(1, 5)
    soma = jog + pc
    poi = str(input('Voce quer par ou ímpar? [P/I] ')).strip().lower()[0]
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    if soma % 2 == 0:
        if poi in 'Pp':
            print('Você ganhou! Parabéns')
            cont += 1
        else:
            print('Você perdeu! Fim de jogo')
            break
    if soma % 2 != 0:
        if poi in 'IiÍí':
            print('Você ganhou! Parabéns')
            cont += 1
        else:
            print('Você perdeu! Fim de jogo')
            break
    print(f'O computador escolheu {pc} e você escolheu {jog}. Total {soma}')
print(f'O computador escolheu {pc} e você escolheu {jog}. Total {soma}')
if cont == 1:
    print(f'Você ganhou {cont} vez somente, antes de perder.')
else:
    print(f'Você ganhou {cont} vezes consecutivas, antes de perder.')
