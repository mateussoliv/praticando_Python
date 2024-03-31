"""

Listas de listas e seus Índices

"""
salas = [
    ['Mateus', 'João'],

    ['Elaine', ],

    ['Rafaela', 'Julia', 'Fabio']
]

# print(salas[2][3][2])


for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)
