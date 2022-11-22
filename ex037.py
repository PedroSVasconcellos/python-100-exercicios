# Exercício Python 037:
# Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

n = int(input('Digite um número inteiro: '))
print('''Para qual das bases você deseja covnerter?
[ 1 ] - Binária
[ 2 ] - Octária
[ 3 ] - Decimal''')
opcao = int(input('Digite sua escolha: '))

if opcao == 1:
    print(f'{n} coonvertido para BINÁRIO é igual a {bin(n)[2:]}')
elif opcao == 2:
    print(f'{n} coonvertido para BINÁRIO é igual a {oct(n)[2:]}')
elif opcao == 3:
    print(f'{n} coonvertido para BINÁRIO é igual a {hex(n)[2:]}')
