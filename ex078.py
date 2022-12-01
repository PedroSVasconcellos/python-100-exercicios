# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []

for c in range(0, 5):
    lista.append(int(input('Digite um número: ')))

print('=' * 30)

print('Você digitou os valores:', end=' ')
for l in lista:
    print(l, end=' ')
print(f'\nO maior valor foi {max(lista)}. ', end='')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'Ele apareceu na posição {i}...')

print(f'O menor valor foi {min(lista)}. ', end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'Ele apareceu na posição {i}...')
