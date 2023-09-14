n = []
for c in range(0,5):
    n.append(int(input(f'Digite o valor da posição {c}: ')))
manor = min(n)
print(f'o maior numero ({max(n)}) apareceu na posição: ',end='')
for i,v in enumerate(n):
    if v == max(n):
        print(f'{i}..',end='')
print(f'\n o menor numero ({min(n)}) apareceu na posição:' ,end='')
for i,v in enumerate(n):
    if v == min(n):
        print(f'{i}..',end='')