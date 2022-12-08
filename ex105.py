# Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber
# várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)


def notas(*n, sit=False):
    """
    -> Função usada para calcular total de notas, maior nota,
    menor nota, média e de forma opcional mostra a situação 'sit'
    :param n: aqui se passam as notas
    :param sit: (opcional) aqui a situação, acima de 7 é boa e abaixo, ruim
    :return: retorna um dicionario com as chaves e seus respectivos valores
    """
    dicionario = {}
    dicionario['total'] = len(n)
    dicionario['maior'] = max(n)
    dicionario['menor'] = min(n)
    dicionario['media'] = sum(n) / len(n)
    if sit:
        if dicionario['media'] < 7:
            dicionario['situação'] = 'RUIM'
        else:
            dicionario['situacao'] = 'BOA'
    return dicionario


resp = notas(9.5, 8.5, 7.5, sit=True)
print(resp)
help(notas)

