# Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104,
# incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.


def leiaint(msginput):
    while True:
        try:
            num = int(input(msginput))
        except (ValueError, TypeError):
            print('\033[31mVocê inseriu um tipo de dado incorreto. Por favor, digite um número inteiro.\033[m')
        except KeyboardInterrupt:
            print('\033[31mO Usuário preferiu não digitar nada.\033[m')
            return 0
        else:
            return num


def leiafloat(msginput):
    while True:
        try:
            num = float(input(msginput))
        except (ValueError, TypeError):
            print('\033[31mVocê inseriu um tipo de dado incorreto. Por favor, digite novamente.\033[m')
        except KeyboardInterrupt:
            print('\033[31mO Usuário preferiu não digitar nada.\033[m')
            return 0
        else:
            return num


nint = leiaint('Digite um número inteiro: ')
nfloat = leiafloat('Digite um número quebrado: ')
print(f'Você acabou de digitar os números \"{nint}\" e \"{nfloat}\".')
