ano = int(input('digite o ano de nascimento: '))
ano = 2023-ano
if ano == 0 and ano <= 9:
    print('nadador mirin')
elif ano == 10 and ano <= 14:
    print('nadador infantil')
elif ano == 15 and ano <= 19:
    print('nadador junior')
elif ano == 20 and ano <= 25:
    print('nadador senior')
elif ano > 25:
    print('nadador master')