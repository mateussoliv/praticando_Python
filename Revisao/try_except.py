numero = input('Vou dobrar o seu numero: ')

try:
    numero_float = float(numero)
    print('FLAT:', numero_float)
    print(f'O dobro de {numero} é {numero_float * 2}')
except:
    print('Isso não é um numero !!!')
