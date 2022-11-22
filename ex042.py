# Exercício Python 042: Refaça o DESAFIO 035 dos triângulos,
# acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Essas retas PODEM formar um triangulo.')
    if r1 == r2 == r3:
        print('O triângulo é EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('O triângulo é ESCALENO')
    else:
        print('O triângulo é ISÓCELES')

else:
    print('Essas retas NÃO podem formar um triangulo.')