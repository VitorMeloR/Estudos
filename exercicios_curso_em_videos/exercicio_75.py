n = (int(input('digite um valor: ')), int(input('digite um valor: ')),
     int(input('digite um valor: ')), int(input('digite um valor: ')),
     int(input('digite um valor: ')))
c9=0
par=[]
print('A tupla digitada foi')
for i in n:
    print(i,end=' ')
    if i == 9:
        c9+=1
    if i % 2 == 0:
        par.append(i)
print(f'\nO numero três foi encontrado na posição {n.index(3)}' if 3 in n else '')
print(f'Foram encontrados os numeros {par} pares nossa tupla')
print(f'Foram encontrados {c9} números nove na nossa tupla')