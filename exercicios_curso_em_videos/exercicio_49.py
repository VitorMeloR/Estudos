tab = int(input('digite um valor para a tabuada: '))
fator = 0
for c in range(0,100):
    fator = fator+1
    tab1 = tab*fator
    print(f'{tab}x{fator}={tab1}')