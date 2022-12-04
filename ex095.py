#Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

cadastro = []
ficha = {}
g = []

while True:
    ficha.clear()
    g.clear()
    ficha['Nome'] = str(input('Nome do Jogador: ')).strip().capitalize()
    part = int(input(f'Quantas partidas {ficha["Nome"]} jogou? '))
    for c in range(1, part + 1):
        g.append(int(input(f'Quantos gols na partida {c}? ')))
    ficha['Gols'] = g[:]
    ficha['Total'] = sum(ficha['Gols'])
    cadastro.append(ficha.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).strip()[0]
        if resp in 'SsNn':
            break
        print('Erro! Digite [S] ou [N].')
    if resp in 'Nn':
        break

print('-=' * 25)
print('cod nome           gols           total ')
print('-' * 40)

for k, v in enumerate(cadastro):
    print(f'{k:<4}{v["Nome"]:<15}{str(v["Gols"]):<15}{v["Total"]}')
while True:
    qual = int(input('Mostrar dados de qual jogador? (999 para sair) '))
    if qual == 999:
        print('Finalizando...')
        break
    elif qual >= len(cadastro):
        print(f'Erro! Não existe jogador com o código {qual}')
    else:
        print('-=' * 20)
        print(f'Levantamento do jogador {cadastro[qual]["Nome"]}:')
        for k, v in enumerate(cadastro[qual]["Gols"]):
            print(f'=> Na partida {k + 1}, fez {v} gols.')
