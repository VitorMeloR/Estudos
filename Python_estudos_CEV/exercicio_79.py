n = list()
while True:
    num = int(input('digite um numero: [999]'))
    if num == 999:
        break
    if num not in n:
        n.append(num)
    else:
        print('já adicionado')
print(n)