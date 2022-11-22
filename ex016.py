# Exercício Python 016
# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.


#forma 1
# from math import trunc
# n = float(input('Digite um número qualquer, quebrado: '))
# print(f'O valor digitado foi {n} e o número sem os decimais é {trunc(n)}')'''

# forma 2
# n = float(input('Digite um número qualquer, quebrado: '))
# print(f'O valor digitado foi {n} e o número sem os decimais é {n:.0f}')

# forma 3
n = float(input('Digite um número qualquer, quebrado: '))
print(f'O valor digitado foi {n} e o número sem os decimais é {int(n)}')


