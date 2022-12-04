# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

lista = []
temp = []
cont = 0

# guarda os valores nas listas
while True:
    nome = str(input('Nome: ')).strip().capitalize()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    temp.append(nome)
    temp.append(n1)
    temp.append(n2)
    lista.append(temp[:])
    temp.clear()
    cont += 1
    r = ' '
    while r not in 'SsNn':
        r = str(input('Quer continuar? [S/N] ')).strip()[0]
    if r in 'Nn':
        break

# mostra total de alunos inseridos e faz decoração
print('-=' * 20)
print(f'Ao total foram inseridos(as) {cont} alunos(as).')
print('-=' * 20)
print(f'{"No.":<5} {"NOME":<10} {"MÉDIA":>5}')
print('-' * 22)

# mostra os valores inseridos nas listas de maneira formatada
for i, l in enumerate(lista):
    media = (l[1] + l[2]) / 2
    print(f'{i:<5} {l[0]:<10} {media:>5}')
print('-=' * 20)

# da informações mais detalhadas sobre o aluno digitado
while True:
    nome = int(input(f'Sobre quem você quer saber? Digite 999 para sair: '))
    if nome == 999:
        break
    for i, l in enumerate(lista):
        if nome == i:
            print('-=' * 20)
            print(f'As notas de {lista[i][0]} são, {lista[i][1]} e {lista[i][2]}')
            print('-=' * 20)
