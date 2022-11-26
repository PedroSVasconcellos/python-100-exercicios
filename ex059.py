# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
acao = 0

while acao != 5:
    print('''O que você deseja fazer com estes números?
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Saber o maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    acao = int(input('Digite sua opção: '))
    if acao == 1:
        print(f'O resultado de {n1} somado a {n2} = {n1 + n2}')
    elif acao == 2:
        print(f'O resultado de {n1} x {n2} = {n1 * n2}')
    elif acao == 3:
        if n1 > n2:
            print(f'O maior número é {n1}')
        elif n2 > n1:
            print(f'O maior número é {n2}')
        elif n2 == n1:
            print(f'{n1} e {n2} são iguais!')
    elif acao == 4:
        print('Digite novos números')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif acao == 5:
        print('Finalizando...')
    else:
        print('Você digitou um comando inválido.')
    sleep(2)

print('O porgrama terminou. Volte sempre')
