sexo = str(input('digite seu sexo[m/f]: ')).strip().lower()
while sexo not in 'mf':
    print('por favor digite da maneira correta')
    sexo = str(input('digite seu sexo[m/f]: ')).strip().lower()
print('foi carai')