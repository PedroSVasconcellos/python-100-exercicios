#Exercício Python 041:
# A Confederação Nacional de Natação precisa de um programa que leia o ano
# de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

from datetime import date

atual = date.today().year
ano = float(input('Digite aqui seu ano de nascimento: '))
idade = atual - ano

print(f'Quem nasceu em {ano:.0f} tem, em {atual}, {idade:.0f} anos.')

if idade <= 9:
    print('Você está na categoria MIRIM')
elif 9 < idade <= 14:
    print('Você está na categoria INFANTIL')
elif 14 < idade <= 19:
    print('Você está na categoria JUNIOR')
elif 19 < idade <=20:
    print('Você está na categoria SÊNIOR')
else:
    print('Você está na categoria MASTER')
