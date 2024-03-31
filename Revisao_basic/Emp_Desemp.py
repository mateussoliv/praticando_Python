# Introdução ao desempacotamento + Tuples

nome = ['Mateus', 'Dos', 'Santos', 'Oliveira']
nome1, nome2, nome3, nome4 = nome


nome2 = ['Rafaela', 'Ribeiro', 'Rodrigues']

fist_name, *_ = nome2

print(nome1)
print(fist_name)
print(_)
