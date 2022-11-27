# Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

nomepreco = ''
precomenor = cont = total = maisdemil = 0

while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Qual o preço? R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        maisdemil += 1
    if cont == 1 or preco < precomenor:
        precomenor = preco
        nomepreco = nome
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if continuar in 'Nn':
        break

print('=' * 20)
print('Compra encerrada!')
print(f'O total gasto na compra foi de R${total:.2f}')
print(f'{maisdemil} produtos custam mais de R$1.000')
print(f'O produto mais barato é {nomepreco.capitalize()}, ele custa {precomenor}')