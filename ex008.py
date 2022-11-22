medida = float(input('Digite uma distância em km que gostaria de converter: '))

hm = medida * 10
dam = medida * 100
m = medida * 1000
dm = medida * 10000
cm = medida * 100000
mm = medida * 1000000

print(f'A distância que você digitou, convertida em hectômetros é igual a: "{hm:.0f} hm" \n'
      f'A distância que você digitou, convertida em decâmetros é igual a: "{dam:.0f} dam" \n'
      f'A distância que você digitou, convertida em metros é igual a: "{m:.0f} m" \n'
      f'A distância que você digitou, convertida em decímetros é igual a: "{dm:.0f} dm" \n'
      f'A distância que você digitou, convertida em centímetros é igual a: "{cm:.0f} cm" \n'
      f'A distância que você digitou, convertida em milímetros é igual a: "{mm:.0f} mm"'
      )
