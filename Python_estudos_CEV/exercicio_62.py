termo = int(input('digite o primeiro termo: '))
razao = int(input('digite a razao: '))
print(f'Esses são os 10 primeiros termos da sua PA')
print(f'{termo}',end=' > ')
mais = 9
a = 9
cout = 0
while True:
    for c in range(0 , mais):
        termo+=razao
        a-=1
        cout+=1
        print(f'{termo} >',end=' ')
    if a == 0:
        print('FIM')
    mais = int(input('\ndeseja adicionar mais quantas razões? [0 para finalizar]'))
    a = mais
    if mais == 0:
        break
print(f'A PA foi finalizada com {cout+1} razões')