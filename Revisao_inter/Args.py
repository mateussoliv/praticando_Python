"""
args - Argumentos não nomeados
* - *args(Empacotamento e Desempacotamento)
"""

# Lembre-te de desempacotamento

x, y, *resto = 1, 2, 3, 4, 5

print(x, y, resto)


def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total


soma(1, 2, 3, 4, 5, 6)
