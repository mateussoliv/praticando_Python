nome = input('Insira seu nome aqui: ')
idade = input('Sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contem Espaçoes em branco')
    else:
        print('Seu nome não contem espacos')

    print(f'Seu nome contem {len(nome)}')
    print(f'A primeira letra do seu nome é {(nome[0])}')
    print(f'A ultima letra é o {(nome[-1])}')
else:
    print('Existem campos em branco')
