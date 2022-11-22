# Exercício Python 026:
# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

# Fui um pouco além e ao inves de tratarmos somente a letra 'A', tratei a primeira letra da frase, que vai variar de frase para frase

frase = input('Digite uma frase: ').strip().upper()

print(f'A primeira letra da frase é {frase[0]} e ela aparece {frase.count(frase[0])} vezes na frase.')
print(f'A primeira letra {frase[0]} apareceu no caracter de posição {frase.find(frase[0]) + 1} pela primeira vez.')
print(f'A última letra {frase[0]} apareceu no caracter de posição {frase.rfind(frase[0]) + 1}.')
