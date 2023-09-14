termo = int(input('digite o primeiro termo: '))
razao = int(input('digite a razao: '))
c = 0
print(f'Esses são os 10 primeiros termos da sua PA')
print(f'{termo}',end=' > ')
while c < 9:
    termo+=razao
    print(f'{termo} >' if c < 8 else f'{termo}',end=' ')
    c+=1