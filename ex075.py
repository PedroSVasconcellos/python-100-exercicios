# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

num = (int(input('Digite o 1o número: ')),
       int(input('Digite o 2o número: ')),
       int(input('Digite o 3o número: ')),
       int(input('Digite o 4o número: ')))

print(f'O valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
       print(f'O primeiro valor 3 apareceu na posição {num.index(3)}.')
else:
       print('Não houve número 3.')
print(f'Os valores pares foram: ', end='')
for n in num:
       if n % 2 == 0:
              print(n, end=' ')
