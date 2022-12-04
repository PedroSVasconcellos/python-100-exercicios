# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

lista = []
temp = []
mai = men = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float  (input('Peso: ')))
    if len(lista) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        elif temp[1] < men:
            men = temp[1]
    lista.append(temp[:])
    temp.clear()
    r = ' '
    while r not in 'SsNn':
        r = str(input('Quer continuar? '))
    if r in 'Nn':
        break

for l in lista:
    if l[1] == men:
        nmen = l[0]

print('=' * 20)
print(f'Foram {len(lista)} pessoas ao todo cadastradas.')
print(f'O maior peso foi {mai}kg. Foi o peso de:', end=' ')
for l in lista:
    if l[1] == mai:
        print(l[0].capitalize(), end=' ')
print(f'\nO menor peso foi {men}kg. Foi o peso de:', end=' ')
for l in lista:
    if l[1] == men:
        print(l[0].capitalize(), end=' ')