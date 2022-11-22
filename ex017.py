# Exercício Python 017:
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

# importando método

from math import hypot

c1 = float(input('Digite aqui o valor do primeiro cateto: '))
c2 = float(input('Digite aqui o valor do segundo cateto: '))

hip = hypot(c1, c2)

print(f'O valor da hipotenusa é {hip:.2f}')

'''
# sem importar metodo

c1 = float(input('Digite aqui o valor do primeiro cateto: '))
c2 = float(input('Digite aqui o valor do segundo cateto: '))

hip = (c1 ** 2 + c2 ** 2) ** 0.5

print(f'O valor da hipotenusa é de {hip:.2f}')
'''