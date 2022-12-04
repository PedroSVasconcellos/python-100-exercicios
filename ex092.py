# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime
cadastro = dict()
cadastro['Nome'] = str(input('Nome: ')).strip().capitalize()
cadastro['Nascimento'] = int(input('Ano de Nascimento: '))
cadastro['Idade'] = datetime.now().year - cadastro['Nascimento']
cadastro['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
if cadastro['CTPS'] == 0:
    print('=' * 10)
    del cadastro['Nascimento']
    for k, v in cadastro.items():
        print(f' - {k} tem o valor {v}')
else:
    cadastro['Contratação'] = int(input('Ano de contratação: '))
    cadastro['Salário'] = int(input('Salário: R$ '))
    cadastro['Aposentadoria'] = (cadastro['Contratação'] - cadastro['Nascimento']) + 35
    print('=' * 10)
    del cadastro['Nascimento']
    for k, v in cadastro.items():
        print(f'  - {k} tem o valor {v}')

