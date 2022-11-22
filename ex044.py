# Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

preco = float(input('O valor a ser pago é de R$ '))

opt = int(input('Temos as seguintes opções: \n'
                    '1 - à vista em dinheiro \n'
                    '2 - à vista no cartão \n'
                    '3 - em até 2x no cartão \n'
                    '4 - 3x ou mais no cartão \n'
                    'Escolha de 1 a 4 como você gostaria de pagar? '))

if opt == 1:
    print('-=-' * 19)
    print(f'À vista em dinheiro/cheque com desconto de 10% - R${preco - preco*10/100:.2f}')
    print('-=-' * 19)
elif opt == 2:
    print('-=-' * 16)
    print(f'À vista no cartão com desconto de 5% - R${preco - preco*5/100:.2f}')
    print('-=-' * 16)
elif opt == 3:
    print('-=-' * 15)
    print(f'Em até 2x no cartão, preço normal - R${preco:.2f}')
    print('-=-' * 15)
elif opt == 4:
    print('-=-' * 20)
    print(f'Em 3x ou mais no cartão com 20% de juros - R${preco + preco*20/100:.2f}')
    print('-=-' * 18)
else:
    print('OPÇÃO INVÁLIDA DE PAGAMENTO. Tente novamente')