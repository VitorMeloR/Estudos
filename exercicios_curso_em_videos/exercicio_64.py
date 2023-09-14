n = int(input('digite quantos termos: '))
t1= 0
t2 = 1
t3 = t1 + t2
print(f'{t1} > {t2} > {t3} > ',end='')
count = 3
while count < n:
    t1 = t2
    t2 = t3
    t3 = t1+t2
    count+=1
    print(f'{t3} > ',end='' if count < n else f'{t3} =')
print('FIM')