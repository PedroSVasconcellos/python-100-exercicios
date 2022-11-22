# Exercício Python 018:
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

angulo = float(input('Qual o valor do ângulo? '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'O ângulo de {angulo} tem o SENO de: {seno:.2f}')
print(f'O ângulo de {angulo} tem o COSENO de: {cosseno:.2f}')
print(f'O ângulo de {angulo} tem a TANGENTE de: {tangente:.2f}')
