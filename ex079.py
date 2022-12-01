# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

numeros = []

while True:
    n = int(input('Digite um valor: '))
    if n in numeros:
        print(f'Valor já digitado, insira outro.')
    else:
        numeros.append(n)
        print(f'Valor adicionado com sucesso.')

    r = ' '
    while r not in 'sn':
        r = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    if r == 'n':
        break
numeros.sort()
print(f'Você digitou os valores: {numeros}')
print(f'Essa lista tem {len(numeros)} elementos.')