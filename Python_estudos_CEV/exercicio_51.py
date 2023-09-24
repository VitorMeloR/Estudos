primeiro = int(input('digite o primeiro termo: '))
razão = int(input('digite a razão: '))
for c in range(1, 11):
    primeiro+=razão
    print(f'{primeiro}',end=' > ')
print('ACABOU')