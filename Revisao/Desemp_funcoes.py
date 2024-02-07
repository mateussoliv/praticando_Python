# Desempacotamento em chamadas de metodos e funlções


string = 'ABCD'
lista = ['Mateus', 'Dos', 'Santos', 'Oliveira']
tupla = ('Python', 'é', 'Legal')

lista.append('Spachi')


for nome in lista:
    print(nome, sep=' ')


print(*lista, end='-')
