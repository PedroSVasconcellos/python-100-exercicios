# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista
# única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

lista = [[], []]

for c in range(1, 8):
    n = int(input(f'Digite o {c}o número: '))
    if n % 2 == 0:
        lista[0].append(n)
        print(lista)
    else:
        lista[1].append(n)
        print(lista)

print(f'Os valores pares são: {sorted(lista[0])}')
print(f'Os valores ímpares são: {sorted(lista[1])}')