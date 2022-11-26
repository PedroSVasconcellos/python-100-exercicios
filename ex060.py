#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

from math import factorial
n = int(input('Digite um número para calcularmos seu fatorial: '))
print(factorial(n))

'''
n = int(input('Digite o número: '))
c = n
f = 1
while c > 1:
    f = f * c
    c -= 1
print(f)
'''