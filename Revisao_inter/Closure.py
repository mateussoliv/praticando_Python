""" 
Closure e funções que retornam outras funções
"""


def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}!'
    return saudar


def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}!'
    return saudar


s1 = criar_saudacao('Bom dia', 'Mateus')

s2 = criar_saudacao('Boa noite', 'Mateus')


print(s1)
print(s2)
