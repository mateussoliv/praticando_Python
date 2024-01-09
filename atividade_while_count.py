frase = 'O rato roeu a roupa do rei de roma'


print(frase.count('r'))

i = 0

while i < len(frase):
    letra_atual = frase[i]
    qts_letra_apareceu = frase.count(letra_atual)

    print(letra_atual, qts_letra_apareceu)

    i += 1
