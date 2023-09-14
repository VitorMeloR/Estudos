from random import randint
c=0
n = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print(f'sortei esses 5 numeros: ', end='')
for i in n:
    print(i,end=' ')
print(f'\no maior numero sorteado foi {(max(n))}')
print(f'o menor numero sorteado foi {min(n)}')