dias = int(input('Quantos dias ficou com o carro? '))
km = float(input('Quantos Km percorreu com o carro? '))

preco = (km * 0.15) + (dias * 60)

print(f'O total ser pago é R${preco:.2f}')

