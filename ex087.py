# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

print('=' * 30)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()

print('=' * 30)

for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    for c in range(2, 3):
        scol += matriz[l][c]
for l in range(1, 2):
    for c in range(0, 3):
        mai = max(matriz[l])

print(f'A soma dos pares é {spar}')
print(f'A soma dos valores da terceira coluna é {scol}')
print(f'O maior valor da segunda linha é {mai}')
