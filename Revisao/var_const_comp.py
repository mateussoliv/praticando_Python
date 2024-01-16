velocidade = float(input('Sua Velocidade: '))
local_carro = float(input('Local: '))


RADAR_1 = 60
RADAR_2 = 100

LOCAL_1 = 120
LOCAL_2 = 200
RADAR_RANGE = 1


if velocidade > RADAR_1:
    print(f'Acima da Velocidade!! Limite: {RADAR_1}')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
   local_carro <= (LOCAL_2 + RADAR_RANGE):
    print('Carro multado')

elif velocidade > RADAR_2:
    print(f'Acima da velocidade Limite:{RADAR_2}')
else:
    print('Dentro do Limite ou fora de Radar...')
