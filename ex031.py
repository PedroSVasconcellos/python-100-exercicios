# Exercício Python 031:
# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('Qual a distância em Km da sua viagem?'))

if distancia <= 200:
    print(f'O preço da sua passagem é de {(distancia * 0.5):.2f} reais')
else:
    print(f'O preço da sua passagem é de {(distancia * 0.45):.2f} reais')

# print(f'O preço da sua passagem é de {(distancia * 0.5):.2f}' if distancia <= 200 else f'O preço da sua passagem é de {(distancia * 0.45):.2f} reais') <--- ALTERNATIVA DE MENOR LEGIBILIDADE
