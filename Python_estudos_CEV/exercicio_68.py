from random import randint
v = 0
print('=+'*30)
print('JOGO DO IMPAR OU PAR')
print('=+'*30)
while True:
    eu = int(input('digite um valor: '))
    pc = randint(0,10)
    total = eu + pc
    pi = input('impar ou par? [p/i]: ').lower().strip()[0]
    while pi not in 'pi':
        pi = input('impar ou par? [p/i]').lower().strip()[0]
    print(f'Você jogou {eu} e o pc jogou {pc}. O total entre você e o pc deu {total}')
    if pi == 'p' and total%2 == 0:
        print('VOCÊ GANHOU')
        v+=1
    if pi == 'i' and total % 2 != 0:
        print('VOCÊ GANHOU')
        v += 1
    else:
        break
    print('vamos jogar novamente...')
print(f'voce perdeu com {v} Vitorias')