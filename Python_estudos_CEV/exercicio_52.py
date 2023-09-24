count = 0
num = int(input('\033[36mdigite um numero e descubre se ele é primo: \033[m'))
for c in range(1,num+1):
    if num%c == 0:
        print(f'\033[32m{c}\033[m',end=" ")
        count+=1
    else:
        print(f'\033[31m{c}\033[m',end=' ')

if count == 2:
    print(f'\n\033[32m O numero {num} é primo\033[m')
if count > 2:
    print(f'\n\033[31mO numero {num} não é primo')
