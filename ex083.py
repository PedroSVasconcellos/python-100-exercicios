# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

exp = str(input('Digite a sua expressão: '))
if exp.count("(") == exp.count(")"):
    print(f'A expressão {exp} é válida.')
else:
    print(f'A expressão {exp} NÃO é válida.')
