# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
    n = lista.append(int(input('Digite um valor: ')))
    r = ' '
    while r not in 'SsNn':
        r = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if r in 'Nn':
        break
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {lista}')
if 5 in lista:
    print(f'O valor 5 está na lista')
else:
    print(f'O valor 5 não está na lista')
