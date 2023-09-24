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
soma_3 = lista[0][2] + lista[1][2] + lista[2][2]
pares=0
print('-='*15)
print(f'{"MATRIZ 3x3":^30}')
for c in range(0,3):
    for i,v in enumerate(lista[c]):
        if v%2 == 0:
            pares+=v
    for i,v in enumerate(lista[c]):
        print(f'{v:^10}',end='')
    print('\n')
print('-='*15)
print(f'A soma dos pares da Matriz: {pares}')
print(f'A soma da terceira coluna: {soma_3}')
print(f'O maior numero da segunda linha: {max(lista[1])}')
print('-='*15)