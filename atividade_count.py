Nome = input('Escreva seu nome: ')
Contagem = len(Nome)

Curto = 4
Normal = 6
Grande = 7

if Contagem <= Curto:
    print(f'Seu nome tem {Contagem} Letras é bem curto em...')

elif Contagem > Curto and Contagem <= Normal:
    print(f'Seu nome tem {Contagem} Letras um tamanho mediano.')

else:
    print(f'Seu nome tem {Contagem} Letras é bem grande!')
