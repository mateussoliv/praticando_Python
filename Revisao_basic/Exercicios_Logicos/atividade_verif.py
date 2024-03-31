Numero = input('Digite o Numero para Verificação: ')

if not Numero:
    print('Informe um numero!!')
else:
    if Numero % 2 == 0:
        print('Este numero é Par')
    else:
        print('Este numero é Impar')
