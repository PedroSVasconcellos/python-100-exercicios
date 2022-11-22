# Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = str(input('Digite aqui seu nome completo: ')).strip()
nomeSplit = nome.split()
print(f'Seu nome com letras maiúsculas: {nome.upper()}')
print(f'Seu nome com letras minúsculas: {nome.lower()}')
print(f'Seu nome tem {len(nomeSplit[0] + nomeSplit[1])} letras ao total, sem considerar espaços.')
print(f'Seu primeiro nome é {nomeSplit[0]} e ele tem {len(nomeSplit[0])} caracteres.')
