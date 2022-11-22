# Exercício Python 034:
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual o seu salário? '))

if salario > 1250:
    print(f'Seu novo salário, com aumento de 10% será de R$ {(salario + salario*10/100):.2f}')
else:
    print(f'Seu novo salário, com aumento de 15% será de R$ {(salario + salario*15/100):.2f}')
