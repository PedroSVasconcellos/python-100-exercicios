# Exercício Python 029:
# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input('Qual a velocidade do carro? '))

if vel > 80:
    print(f'Você estava acima do limite e foi MULTADO em R${((vel - 80) * 7):.2f}')

print('Tenha um bom dia, dirija com segurança!')
