# Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

idadeTotal = 0
nomeMaisVelho = 0
idadeMaisVelho = 0
mulheresMenos20 = 0

for p in range(1, 6):
    print(f'----- {p}a PESSOA -----')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip()
    idadeTotal += idade
    if p == 1 and sexo in 'Mm':
        nomeMaisVelho = nome
        idadeMaisVelho = idade
    if sexo in "Mm" and idade > idadeMaisVelho:
        idadeMaisVelho = idade
        nomeMaisVelho = nome
    if sexo in "Ff" and idade < 20:
        mulheresMenos20 += 1

mediaIdade = idadeTotal / p

print(f'A média das idades é de {mediaIdade:.1f}')
print(f'O nome do homem mais velho é {nomeMaisVelho} e ele tem {idadeMaisVelho} anos.')
if mulheresMenos20 == 1:
    print(f'Existe {mulheresMenos20} mulher abaixo de 20 anos.', )
elif mulheresMenos20 > 1:
    print(f'Existem {mulheresMenos20} mulheres abaixo de 20 anos.')

