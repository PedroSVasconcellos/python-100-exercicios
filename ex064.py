# Exercício Python 064:
# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final,
# mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

n2 = cont = 0
n = int(input('Digite um número [999 para encerrar]: '))
while n != 999:
    n2 += n
    cont += 1
    n = int(input('Digite um número [999 para encerrar]: '))
print(f'Você digitou {cont} números. A soma entre eles foi {n2}')


# outra maneira
'''n = n2 = cont = 0
while n != 999:
    n = int(input('Digite um número [999 para encerrar]: '))
    if n != 999:
        n2 += n
        cont += 1
print(f'A soma dos números digitados foi {n2}')'''