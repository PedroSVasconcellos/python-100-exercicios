# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM',
# o programa se encerrará. Importante: use cores.


def funcTitulo(titulo):
    print(f'\033[1:30:42m~' * (len(titulo) + 4))
    print(f'  {titulo}')
    print(f'~' * (len(titulo) + 4))
    print(f'\033[m', end='')


def funcSubTitulo(subTitulo):
    print(f'\033[7:34m~' * (len(subTitulo) + 4))
    print(f'  {subTitulo}')
    print(f'~' * (len(subTitulo) + 4))
    print(f'\033[m', end='')


def funcPesquisa(item):
    funcSubTitulo(f'Acessando o manual do comando "{item}"')
    print(f'\033[7m')
    print(help(f'{item}'))
    print(f'\033[m')


while True:
    funcTitulo('SISTEMA DE AJUDA PyHELP')
    itemPesquisa = str(input('Função ou Biblioteca a pesquisar: ')).strip().lower()
    if itemPesquisa == 'fim':
        break
    else:
        funcPesquisa(itemPesquisa)

