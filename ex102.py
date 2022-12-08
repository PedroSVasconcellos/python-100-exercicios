# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.


def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número
    :param n: número do fatorial a ser calculado
    :param show: (opcional) True se quiser ver a conta feita, padrão False
    :return: valor do Fatorial do número "n"
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            if c > 1:
                print(f'{c} x ', end='')
            else:
                print(f'{c} =', end=' ')
    print(f'{f}')
    return f


fatorial(5, show=True)
help(fatorial)