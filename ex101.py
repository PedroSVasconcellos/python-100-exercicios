# Nessa aula, vamos continuar nossos estudos de funções em Python, aprendendo mais sobre Interactive Help em Python,
# o uso de docstrings para documentar nossas funções, argumentos opcionais para dar mais dinamismo em funções Python,
# escopo de variáveis e retorno de resultados.


def voto(a):
    from datetime import datetime
    idade = datetime.now().year - a
    if 16 <= idade < 18:
        return f'{idade} anos, voto OPCIONAL.'
    elif 18 <= idade < 65:
        return f'{idade} anos, voto OBRIGATÓRIO.'
    elif idade < 16:
        return f'{idade} anos, muito cedo ainda. Não pode votar.'
    elif idade >= 65:
        return f'{idade} anos, voto OPCIONAL.'


while True:
    ano = int(input('Em que ano você nasceu? '))
    if ano == 999:
        print('Fim')
        break
    print(voto(ano))
