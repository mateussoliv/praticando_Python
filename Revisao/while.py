# contador = 0


# while contador <= 10:
#     contador += 1

#     if contador == 6:
#         print('Sem o 6')
#         continue

#     if contador == 8:
#         break

#     print(contador)

# print('Acabou')


qtd_linhas = 5

qts_colunas = 5

linha = 1
coluna = 1

while linha <= qtd_linhas:

    while coluna <= qts_colunas:
        print(f'{linha=}, {coluna=}')
        coluna += 1

    linha += 1


print('Acabou')
"""
Iterando string com while
"""

nome = 'Mateus Oliveira'

indice = 0
novo_nome = ''

while indice < len(nome):
    letra = nome[indice]
    novo_nome += letra
    indice += 1

print(novo_nome)
