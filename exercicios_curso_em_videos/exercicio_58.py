from time import sleep
from random import choice
n = [1,2,3,4,5,6,7,8,9,10]
maq = choice(n)
print('\033[0:36m-='*100)
print('Vou pensar em um número entre 0 e 5. Tente advinhar em 3 jogadas')
print('=-'*100)
parametro = 0
count = 0
while not parametro == 1:
    num = int(input('\033[0:36mEm que numero pensei? \033[m'))
    print('\033[0:33mPROCESSANDO...\033[m')
    sleep(2)
    count+=1
    if num == maq:
        print(f'\033[0:32mVocê com {count} palpites acertou o número que eu pensei ({maq}) você GANHOU!!\033[m')
        parametro = 1
    elif num != maq and num < maq:
        print(f'\033[0:31mEstá perto. digite um numero maior\033[m')
    elif num != maq and num > maq:
        print(f'\033[0:31mEstá perto. digite um numero menor\033[m')
    print('\033[0:36m=-\033[m'*100)