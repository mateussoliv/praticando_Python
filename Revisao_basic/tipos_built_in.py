# Repetiçoes
# while  (Enquanto)
# Executa uma ação enquanto uma condicao for verdadeira

condicao = True

while condicao:
    nome = input('Qual é seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair' or nome == 'Sair':
        break

print('Muito Obrigado')
