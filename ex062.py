# Exercício Python 062:
# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

primeiro = int(input('Digite o primeiro número: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print(termo, end=' ->')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais? '))

print(f'FIM. Você exibiu um total de {total} termos.')
