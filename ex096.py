# Exercício Python 096: Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(a, b):
    area = a * b
    print(f'A área de um terreno com {a}m de largura por {b}m de comprimento = a {area}m2')


larg = int(input('Largura (m): '))
comp = int(input('Comprimento (m): '))
area(larg, comp)