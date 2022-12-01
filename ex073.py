# Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da
# Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time do Santos.

camp = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo',
        'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG',
        'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá',
        'Ceará', 'Atletico-GO', 'Avaí', 'Juventude')
print('-=' * 40)
print(f'Lista de times do Brasileirão 22: {camp}')
print('-=' * 40)
print(f'Os 5 primeiros são: {camp[0:5]}')
print('-=' * 40)
print(f'Os 4 últimos são {camp[-4:]}')
print('-=' * 40)
print(f'Times em ordem alfabética: {sorted(camp)}')
print('-=' * 40)
print(f'O Santos terminou o campeonato na {camp.index("Santos") + 1}a posição.')