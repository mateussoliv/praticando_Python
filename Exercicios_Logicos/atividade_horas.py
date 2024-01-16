Horario = int(input('Me informe o horario sem os minutos: '))

Dia = 11
Tarde = 17
Noite = 23

if Horario <= Dia:
    print(f'Olá Bom dia são {Horario} Hrs, tudo bem?')

elif Horario > Dia and Horario <= Tarde:
    print(f'Olá Boa tarde são {Horario} Hrs, Já almocou?')

else:
    print(f'Boa Noite são {Horario} Hrs, Vai dormir ?')
