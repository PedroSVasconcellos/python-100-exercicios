# Exercício Python 046:
# Faça um programa que mostre na tela uma contagem regressiva para oestouro
# de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.


from time import sleep
from emoji import emojize

cr = int(input('De quantos segundos será a contagem regressiva? '))

print(emojize(':hourglass:', language='alias'), ' Contando!')

for c in range(cr, -1, -1):
    print(c, end='')
    print(' - ', end='')
    sleep(1)
print(emojize(':boom:', language='alias'))
