numeros = [[],[]]
print('-='*15)
for c in range(0,7):
    while True:
        n = input(f'Digite o {c+1}° numero inteiro: ').strip()
        try:
            n = int(n)
            break
        except ValueError as err:
            print('tente novamente')
    if n%2==0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
print('-='*15)
for i,v in enumerate(sorted(numeros[0])):
    if i == 0:
        print(f'{"NUMEROS PARES":^30}')
    print(f'{v}',end=' ')
print('\n')
for i,v in enumerate(sorted(numeros[1])):
    if i == 0:
        print('-='*15)
        print(f'{"NUMEROS IMPARES":^30}')
    print(f'{v}',end=' ')
print('\n')
print('-='*15)