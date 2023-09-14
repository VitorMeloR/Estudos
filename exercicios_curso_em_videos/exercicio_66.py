print('-'*33)
while True:
    n = int(input('quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('-'*33)
    for c in range(1,11):
        tab = n*c
        print(f'{n} x {c} = {tab}')
        if c == 10:
            print('-'*33)
print('programa encerrado')