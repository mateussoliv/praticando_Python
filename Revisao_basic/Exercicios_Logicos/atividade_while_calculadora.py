""" Calculadora com while """

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+, -, /, *): ')

    numeros_validos = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True

    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Os números podem estar invalidos!!!')
        continue

    ###

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido!')
        continue

    if len(operador) > 1:
        print('Selecione apenas um operador!!!')
        continue

    ###
    if operador == '+':
        print(f'O resultado é {num_1_float + num_2_float}')
    elif operador == '-':
        print(f'O resultado é {num_1_float - num_2_float}')
    elif operador == '/':
        print(f'O resultado é {num_1_float / num_2_float}')
    elif operador == '*':
        print(f'O resultado é {num_1_float * num_2_float}')

    else:
        print('Algo esta errado 🙏🙏🙏🙏🙏')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        print('Saindo...')
        break
