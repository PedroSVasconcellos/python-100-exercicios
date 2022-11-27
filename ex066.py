# Exercício Python 066: Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

contNum = somaNum = 0
while True:
    n = int(input('Digite um número inteiro (999 se quiser parar): '))
    if n == 999:
        break
    contNum += 1
    somaNum += n
print(f'Você digitou ao total {contNum} númweos e a soma deles é {somaNum}.')
