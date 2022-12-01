# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

lista = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')

for p in lista:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for l in p:
        if l in 'aeiou':
            print(l, end=' ')
