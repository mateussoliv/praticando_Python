# enumerate - enumera os iteráveis (índices)
import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar: ')
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor, digite apenas um numero int.')
        except IndexError:
            print('Por favor, apenas numeros Int.')
    elif opcao == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('Nada na Lista')

        for i, valor in enumerate(lista):
            print(i, valor)
