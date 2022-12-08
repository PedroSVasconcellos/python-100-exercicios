# Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma
# semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n: ')


def leiaint(num):
    while True:
        t = str(input(num)).strip()
        if t.isnumeric():
            t = int(t)
            return t
        else:
            print(f'\033[31mErro! Digite um número inteiro válido.\033[m')


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
