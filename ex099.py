# Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(* n):
    cont = maior = 0
    print(f'\nAnalizando os valores passados...')
    for valor in n:
        print(valor, end=' ')
        if cont == 0:
            cont += 1
            maior = valor
        else:
            cont += 1
            if valor > maior:
                maior = valor

    print(f'O maior valor é --> {maior}')


maior(1, 4, 3, 2, 5)
maior(2, 4, 3, 6)
maior(1, 2, 6)