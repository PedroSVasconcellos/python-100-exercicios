# Exercício Python 045:
# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
computador = randint(0, 2)
itens = ('Pedra', 'Papel', 'Tesoura')

print('''Vamos jogar!
[ 0 ] - Pedra
[ 1 ] - Papel
[ 2 ] - Tesoura''')
jogador = int(input('Digite a sua escolha: '))

print('-=' * 15)
print(f'O jogador escolheu \033[33m{itens[jogador]}\033[m')
print(f'O computador escolheu \033[33m{itens[computador]}\033[m')
print('-=' * 15)

if computador == 0: # Computador PEDRA
    if jogador == 0:
        print('Deu \033[33mEMPATE\33[m')
    elif jogador == 1:
        print('Jogador \033[32mVENCEU\033[m')
    elif jogador == 2:
        print('Jogador \033[31mPERDEU\033[m')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: # Computador PAPEL
    if jogador == 0:
        print('Jogador \033[31mPERDEU\033[m')
    elif jogador == 1:
        print('Deu \033[33mEMPATE\33[m')
    elif jogador == 2:
        print('Jogador \033[32mVENCEU\033[m')
elif computador == 2: # Computador TESOURA
    if jogador == 0:
        print('Jogador \033[32mVENCEU\033[m')
    elif jogador == 1:
        print('Jogador \033[31mPERDEU\033[m')
    elif jogador == 2:
        print('Deu \033[33mEMPATE\33[m')
    else:
        print('JOGADA INVÁLIDA!')


# código com strings ao inves de numeral
'''
from random import randint
jogador = input('Você escolhe pedra, papel ou tesoura? ').strip().lower()
maquina = randint(1, 3)

#empates
if maquina == 1 and jogador == 'pedra':
    print(f'Você escolheu {jogador.capitalize()} e a máquina escolheu {"Pedra"}')
    print('Deu EMPATE')
if maquina == 2 and jogador == 'papel':
    print(f'Você escolheu {jogador.capitalize()} e a máquina escolheu {"Papel"}')
    print('Deu EMPATE')
if maquina == 3 and jogador == 'tesoura':
    print(f'Você escolheu {jogador.capitalize()} e a máquina escolheu {"Tesoura"}')
    print('Deu EMPATE')

# jogador escolhendo papel
if maquina == 3 and jogador == 'papel':
    print(f'Você escolheu {jogador.capitalize()} e a máquina escolheu {"Tesoura"}')
    print('Você PERDEU')
if maquina == 1 and jogador == 'papel':
    print(f'Você escolheu {jogador.capitalize()} e a máquina escolheu {"Pedra"}')
    print('Você VENCEU')

# jogador escolhendo tesoura
if maquina == 1 and jogador == 'tesoura':
    print(f'Você escolheu {jogador.capitalize()} e a máquina escolheu {"Pedra"}')
    print('Você PERDEU')
if maquina == 2 and jogador == 'tesoura':
    print(f'Você escolheu {jogador.capitalize()} e a máquina escolheu {"Papel"}')
    print('Você VENCEU')

# jogador escolhendo pedra
if maquina == 2 and jogador == 'pedra':
    print(f'Você escolheu {jogador.capitalize()} e a máquina escolheu {"Papel"}')
    print('Você PERDEU')
if maquina == 3 and jogador == 'pedra':
    print(f'Você escolheu {jogador.capitalize()} e a máquina escolheu {"Tesoura"}')
    print('Você VENCEU')
'''
