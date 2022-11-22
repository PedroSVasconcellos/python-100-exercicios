# Exercício Python 027:
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite aqui seu nome completo: ')).strip().split()
print(f'Seu primeiro nome é: {nome[0]}')
print(f'Seu último nome é: {nome[-1]}')
#  print(f'Seu último nome é: {nome[len(nome) - 1]}') <--- outra maneira de resolver, menos 1 pois len conta a partir de 1 e lista conta a partir de 0
