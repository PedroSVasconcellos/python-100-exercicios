#Exercício Python 039:
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

ano = int(input('Em que ano você nasceu? '))
alistamento = ano + 18
anoAtual = 2022

print(f'Quem nasceu em {ano} tem \033[36m{anoAtual - ano}\033[m anos em {anoAtual}.')

if alistamento == anoAtual:
    print('Você deve se alistar agora!')
elif alistamento < anoAtual:
    print(f'Você deveria ter se alistado há \033[31m{anoAtual - alistamento}\033[m anos atrás. \n'
          f'Seu alistamento deveria ter sido em {alistamento}')
elif alistamento > anoAtual:
    print(f'Você deverá se alistar em \033[33m{abs(anoAtual - alistamento)}\033[m anos.')
