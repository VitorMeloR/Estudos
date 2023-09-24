km = float(input('qual a distancia distancia da sua viagem? '))
print(f'você está prestes a começar uma viagem de {km}km')
if km >= 200:
    custo = km*0.45
    print(f'sua viagem de {km}km ficará em R${custo}')
else:
    custo = km*0.50
    print(f'sua viagem de {km}km ficará em R${custo}')