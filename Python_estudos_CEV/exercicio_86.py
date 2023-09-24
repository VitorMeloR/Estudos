lista = [[],[],[]]
for c in range(0,3):
    for i in range(0,3):
        while True:
            n=input(f'Digite o numero da matriz [{i} , {c}]: ')
            try:
                n=int(n)
                break
            except ValueError as err:
                print('Por favor, digite numeros inteiros')
        lista[c].append(n)
print('-='*15)
print(f'{"MATRIZ 3x3":^30}')
for c in range(0,3):
    for i,v in enumerate(lista[c]):
        print(f'{v:^10}',end='')
    print('\n')
print('-='*15)