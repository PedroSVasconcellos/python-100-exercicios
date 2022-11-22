#Exercício Python 049:
# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n = int(input('Digite um número para ver a tabuada dele: '))
for t in range(0, 11):
    print(f'{n} X {t} = {n * t}')
