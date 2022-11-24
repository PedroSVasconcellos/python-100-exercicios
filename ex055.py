#Exercício Python 055:
# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

lista = []
for c in range(1, 6):
    peso = float(input(f'Digite o peso da {c} pessoa: '))
    lista.append(peso)
lista.sort()
print(f'O menor peso é de {lista[0]} ')
lista.sort(reverse=True)
print(f'O menor peso é de {lista[0]} ')
