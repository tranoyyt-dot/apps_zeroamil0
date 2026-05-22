while True: 
    texto = input('Digite um número:')
    if texto == 's':
        break
    numero = int(texto)
    if numero % 2 == 0:
        continue
    print(numero, " é par seu quadrado é ", numero * numero)