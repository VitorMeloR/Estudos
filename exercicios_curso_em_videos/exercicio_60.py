n =int(input('digite um numero a ser fatorial: '))
c = n
fatorial = 1
while c > 0:
    print(f'{c} =' if c == 1 else f'{c} x',end=' ')
    fatorial *= c
    c-=1
print(fatorial)