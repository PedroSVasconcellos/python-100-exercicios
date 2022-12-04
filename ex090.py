# Nessa aula, vamos aprender o que são DICIONÁRIOS e como utilizar dicionários em Python.
# Os dicionários são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves literais.

dic = dict()
dic['Nome'] = str(input('Nome: ')).strip().capitalize()
dic['Media'] = float(input(f'Média de {dic["Nome"]}: '))
if 5 <= dic['Media'] < 7:
    dic['Situação'] = 'RECUPERAÇÃO'
elif dic['Media'] < 5:
    dic['Situação'] = 'REPROVADO'
else:
    dic['Situação'] = 'APROVADO'
print('-' * 20)
for k, v in dic.items():
    print(f'{k} é igual a {v}')
