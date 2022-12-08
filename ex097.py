# Exercício Python 097: Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.


def escrita(string):
    linha = '~' * (len(string) + 10)
    print(linha)
    print(f'     {string}')
    print(linha)


l = 'Pedro da Bahia'
escrita(l)
