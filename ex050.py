# Exercício Python 050:
# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

cont = 0
final = 0
for c in range(0, 6):
    num = int(input('Digite un número: '))
    if num % 2 == 0:
        final += num
        cont += 1
if cont == 1:
    print(f'Você digitou {cont} número par. Este número foi: {final}')
else:
    print(f'Você digitou {cont} números pares. A soma dos numeros pares é: {final}')
