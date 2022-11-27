# Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

# com uso de if/else
pergunta = 's'
maior = menor = total = cont = 0

while pergunta == 's':
    n = int(input('Digite um número: '))
    cont += 1
    total += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

    pergunta = str(input('Quer continuar? [S/N] ')).strip().lower()[0]

media = total / cont
print(f'Você digitou {cont} números e a média entre eles é {media:.1f}')
print(f'Dos números digitados, {menor} foi o menor e o maior deles foi {maior}.')


# com uso de lista
'''
pergunta = 's'
total = cont = 0
todos = []

while pergunta == 's':
    n = int(input('Digite um número: '))
    cont += 1
    total += n
    todos.append(n)
    pergunta = str(input('Quer continuar? [S/N] ')).strip().lower()[0]

media = total / cont
todos.sort()

print(f'o menor número digitado foi {todos[0]}')
print(f'o maior número digitado foi {todos[-1]}')
print(f'Você digitou {cont} números e a média entre eles é {media}')
'''





