#Exercício Python 054:
# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
maiores = 0
menores = 0
for c in range(0, 5):
    ano = int(input('Em que ano você nasceu? '))
    if (date.today().year - ano) >= 21:
        maiores += 1
    else:
        menores += 1
print(f'Considerando 21 anos como maioridade, {menores} são menores de idade e {maiores} são maiores de idade.')
