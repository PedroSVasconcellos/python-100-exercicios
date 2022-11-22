#Exercício Python 040:
# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:

n1 = float(input('Qual foi a sua primeira nota? '))
n2 = float(input('Qual foi a sua segunda nota? '))
media = (n1 + n2) / 2

print('-=-' * 10)
print('A média final foi:', media)
if media < 5:
    print(f'O aluno foi \033[31mREPROVADO\033[m')
elif media >= 7:
    print('O aluno foi \033[32mAPROVADO\033[m')
else:
    print('O aluno está de \033[33mRECUPERAÇÃO\033[m')
