# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep

dic = {'Jogador 1': randint(1, 6),
    'Jogador 2': randint(1, 6),
    'Jogador 3': randint(1, 6),
    'Jogador 4': randint(1, 6)}

for k, v in dic.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)

#usado pra ordenar o dicionario transformando ele em lista
ranking = sorted(dic.items(), key=lambda item: item[1], reverse=True)
print('-=' * 15)
sleep(0.5)

for k, v in enumerate(ranking):
    print(f'{k + 1}o lugar: {v[0]} com {v[1]}')
    sleep(0.5)

