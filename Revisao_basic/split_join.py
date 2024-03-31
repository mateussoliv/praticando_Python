"""
    split e join com list e str

    split - divide uma string
    join - une uma string    

"""

frase = '     Olha só que,       coisa interessante'

lista_frases = frase.split(',')


lista_frases_fixed = []

for i, frase in enumerate(lista_frases):
    lista_frases_fixed.append(lista_frases[i].strip())


print(lista_frases)
print(lista_frases_fixed)


frases_unidas = '-'.join(lista_frases_fixed)
print(frases_unidas)
