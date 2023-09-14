from random import randint
mega = list()
print('-='*15)
print(f'{"PALPITES PARA MEGA":^30}')
print('-='*15)
while True:
    jogos = input('Quantos jogos você gostaria de fazer?\nR:')
    try:
        jogos = int(jogos)
        break
    except ValueError as err:
        print('Digite apenas numeros por favor')
for j in range(0,jogos):
    c=0
    mega.append(list())
    while c < 6:
        num = randint(1, 60)
        if num not in mega[j]:
            mega[j].append(num)
            c+=1
print('-='*15)
print(f'{"JOGOS SORTEADOS":^30}')
print('-='*15)
i=0
for v in range(0,len(sorted(mega))):
    print('-='*15)
    print(f'           JOGO {v}')
    ord = sorted(mega[v])
    for c in range(1,61):
        if ord[i] == c:
            print(f'\033[32m{c:02d}\033[m',end=' ')
            i+=1
        else:
            print(f'{c:02d}',end=' ')
        if c%10 == 0:
            print('\n')
        elif i == 6:
            i=0
    print(f'{"GABARITO":^30}')
    print(ord)
