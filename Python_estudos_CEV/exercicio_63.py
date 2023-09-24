soma = count = 0
while True:
    n = int(input('digite um numero: [999 para parar]'))
    if n == 999:
        break
    else:
        soma+=1
        count+=1
print(f'você digitou {count} numeros e  a soma entre eles é de {soma}')