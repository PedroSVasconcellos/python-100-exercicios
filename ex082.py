# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista = []
listapar = []
listaimpar = []

while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)
    r = ' '
    while r not in 'SsNn':
        r = str(input('Quer continuar? [S/N] ')).strip()[0]
        if r not in 'SsNn':
            print('Por favor, [S] ou [N].')
    if r in 'Nn':
        break

print(f'A lista com todos os números é: {lista}')
print(f'A lista com os números pares é: {listapar}')
print(f'A lista com os números impares é: {listaimpar}')