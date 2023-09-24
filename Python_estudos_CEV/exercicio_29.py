kmh = int(input('\033[0:36mqual a velocidade? \033[m'))
if kmh <= 80:
    print(f'\033[0:32mvocê não passou do limite de velocidade. Tenha um bom dia\033[m')
elif kmh > 80:
    multa = kmh-80
    multa = 7*multa
    print(f'\033[0:31mvocê passou do limite e recebeu uma multa de R${multa}\033[m')