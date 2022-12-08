# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função
# vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint

print('=' * 60)
def sorteio(numeros):
    for c in range(0, 5):
        numeros.append(randint(0, 9))
    print(f'Sorteando os 5 valores da lista temos: {numeros} ')


def somapares(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = []
sorteio(numeros)
somapares(numeros)


