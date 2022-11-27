# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

# adicionei notas de R$100 e R$5 também
# usando while e if, como o professor ensinou

din = int(input('Digite o valor que você deseja sacar: '))
ced = 100
totced = 0
print('-' * 20)
while True:
    if din >= ced:
        din -= ced
        totced += 1
    else:
        if totced >= 1:
            print(f'{totced} cédulas de R$ {ced}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        if din == 0:
            break
        totced = 0
print('-' * 20)
print('Obrigado por utilizar nosso banco')


# ======================
# usando divisão e resto
# ======================
'''
din = int(input('Quanto você quer sacar? R$ '))
ced100 = din // 100
ced50 = (din % 100) // 50
ced20 = ((din % 100) % 50) // 20
ced10 = (((din % 100) % 50) % 20) // 10
ced05 = ((((din % 100) % 50) % 20) % 10) // 5
ced01 = (((((din % 100) % 50) % 20) % 10) % 5) // 1
print(f'{ced100} notas de 100\n{ced50} notas de 50\n{ced20} notas de 20\n{ced10} notas de 10\n{ced05} notas de 5\n{ced01} notas de 1')
'''