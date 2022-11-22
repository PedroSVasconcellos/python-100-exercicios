# Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

peso = float(input('Digite aqui seu PESO (kg): '))
altura = float(input('Digite aqui sua ALTURA (m): '))

imc = peso / altura**2

if imc <= 18.5:
    print(f'Seu IMC é de {imc:.1f} Seu índice aponta - abaixo do peso ideal.')
elif 18.5 < imc <= 25:
    print(f'Seu IMC é de {imc:.1f} Seu índice aponta - peso ideal.')
elif 25 < imc <= 30:
    print(f'Seu IMC é de {imc:.1f} Seu índice aponta - sobrepeso.')
elif 30 < imc <= 40:
    print(f'Seu IMC é de {imc:.1f} Seu índice aponta - obesidade.')
else:
    print(f'Seu IMC é de {imc:.1f} Seu índice aponta - obesidade mórbida.')
