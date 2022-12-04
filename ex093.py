# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato.

ficha = {}
g = []
ficha['Nome'] = str(input('Nome do Jogador: ')).strip().capitalize()
part = int(input(f'Quantas partidas {ficha["Nome"]} jogou? '))
for c in range(1, part + 1):
    g.append(int(input(f'Quantos gols na partida {c}? ')))
ficha['Gols'] = g[:]
ficha['Total'] = sum(ficha['Gols'])
print('-=' * 20)
print(ficha)
print('-=' * 20)
for k, v in ficha.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 20)
print(f'O jogador {ficha["Nome"]} jogou {part} partidas')
for k, v in enumerate(ficha['Gols']):
    print(f'=> Na partida {k + 1}, fez {v} gols.')



