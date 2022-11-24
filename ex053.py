# Exercício Python #053 - Detector de Palíndromo

frase = str(input('Digite aqui uma frase para saber se ela é um palíndromo: ')).strip().lower()
frase = ''.join(frase.split())
fraseAoContrario = frase[::-1]

print(f'O inverso de "{frase}" é "{fraseAoContrario}"')

if frase == fraseAoContrario:
    print('Esta frase é um \033[32mPALÍNDROMO\033[m!')
else:
    print('Esta frase é \033[31mNÃO\033[m é um PALÍNDROMO!')
