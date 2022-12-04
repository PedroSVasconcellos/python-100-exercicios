# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

cadastro = []
ficha = {}
totidade = media = 0
while True:
    ficha.clear()
    ficha['Nome'] = str(input('Nome: ')).strip().capitalize()
    while True:
        ficha['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if ficha['Sexo'] in 'MF':
            break
        print('Erro! Digite [M] ou [F].')
    ficha['Idade'] = int(input('Idade: '))
    cadastro.append(ficha.copy())
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('Erro! Digite [S] ou [N].')
    if continuar == 'N':
        break
for c in cadastro:
    totidade += c['Idade']
media = totidade / len(cadastro)
print('-=' * 50)
print(f'A) Ao todo temos {len(cadastro)} pessoas cadastradas.')
print(f'B) A média da idade é {media} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')
for c in cadastro:
    if c['Sexo'] == 'F':
        print(c['Nome'], end='... ')
print(f'\nD) As pessoas que estão acima da média de idade são:')
for c in cadastro:
    if c['Idade'] > media:
        print(f'     nome = {c["Nome"]}; sexo = {c["Sexo"]}; idade = {c["Idade"]};')
