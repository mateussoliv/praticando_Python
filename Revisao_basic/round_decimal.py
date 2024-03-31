# Imprecisão de ponto flutuante

import decimal  # Usar quando for preciso usar todos os numeros decimais.

numero_1 = decimal.Decimal(0.1)
numero_2 = decimal.Decimal(0.7)
numero_3 = numero_1 + numero_2


print(numero_3)
print(f'{numero_3:.2f}')  # Exibe o numero formatado.
# Arredonda o numero, o numero ao lado corta os demais.
print(round(numero_3, 2))
