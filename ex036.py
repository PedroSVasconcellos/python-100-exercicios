# Exercício Python 036:
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.


valorCasa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? R$ '))
anos = float(input('Em quantos anos planeja pagar a casa? '))
meses = anos * 12

parcelaMes = valorCasa / meses

if parcelaMes <= salario*30/100:
    print(f'Seu salário é de R${salario:.2f} e a parcela serã de R${parcelaMes:.2f}. O seu empréstimo foi aprovado!')
else:
    print(f'Seu salário é de R${salario:.2f} e a parcela serã de R${parcelaMes:.2f}. O seu empréstimo foi negado!')
