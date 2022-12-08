# Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
# início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
from time import sleep


def contador(i, f, p):
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        for c in range(i, f+1, p):
            print(c, end=' ')
            sleep(0.25)
        print('FIM')
        print('-=' * 20)
    else:
        cont = i + p
        while cont > f:
            cont -= p
            print(cont, end=' ')
            sleep(0.25)
        print('FIM')
        print('-=' * 20)


contador(0, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Personalize você a contagem!')
print('-=' * 20)
ini = int(input('Início: '))
fim = int(input('Final: '))
pul = int(input('Pulando: '))
contador(ini, fim, pul)
