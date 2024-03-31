
def multiplica_args(*args):
    total = 1
    for valor in args:
        total *= valor
    print('Valores da Varivel: ', total)

    return total


resultado = multiplica_args(2, 3, 4)
print('Resultado Final: ', resultado)


def par_impar(numero):
    return numero % 2 == 0


print(par_impar(2))
print(par_impar(3))


def impar_par(numero1):
    resto = numero1 % 2 == 0

    if resto:
        return f'{numero1} é par'
    return f'{numero1} é impar'


print(impar_par(2))
print(impar_par(3))
