from time import sleep
from random import choice
while True:
    print('\033[0:36m-='*100)
    print('Vou pensar em um número entre 0 e 5. Tente advinhar em 3 jogadas')
    print('=-'*100)
    num = int(input('Em que numero pensei? \033[m'))
    n = [0,1,2,3,4,5]
    maq = choice(n)
    print('\033[0:33mPROCESSANDO...\033[m')
    sleep(2)
    if num == maq:
        print(f'\033[0:32mVocê GANHOU o número que eu pensei foi {maq} e você ACERTOU!!\033[m')
    elif num != maq:
        print(f'\033[0:31mGANHEI! Eu pensei no número {maq} e não no {num}\033[m')
    print('\033[0:36m=-\033[m'*100)
    breaks = str(input('\033[0:36mDeseja terminar o jogo [s/n}: \033[m'))
    print('\033[0:36m=-\033[m' * 100)
    if breaks == 's':
        break
print(f'\033[0:36m{"Jogo encerrado. Obrigado por jogar":^100}\033[m')