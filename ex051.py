#Exercício Python 051:
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.print('-=' * 20)

print(f"{'10 TERMOS DE UMA PA':^40}")
print('-=' * 20)

p = int(input('Digite aqui o primeiro número: '))
r = int(input('Digite aqui a razão: '))

for c in range(p, p + (10 * r), r):
    print(f'{c} --> ', end="")
print('FINAL')
