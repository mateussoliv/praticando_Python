import os

palavra_secreta = 'rafaela'
letras_acertadas = ''
numero_tentativas = 0

while True:
    lentra_digitada = input('Envie uma letra: ')
    numero_tentativas += 1

    if len(lentra_digitada) > 1:
        print('Digite Apenas uma letra.')

        continue

    if lentra_digitada in palavra_secreta:
        letras_acertadas += lentra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('!!!!!! PARABENS VOCE ENCONTROU !!!!!!!')
        print(f'Voce tentou, {numero_tentativas} Vezes')
        print(f'A palavra era: {palavra_secreta}')
        letras_acertadas = ''
        numero_tentativas = 0
        break
