# Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print(f'Um erro ocorreu. O site não pôde ser acessado.')
else:
    print(f'Deu certo! O site está online')
    print(site.read())