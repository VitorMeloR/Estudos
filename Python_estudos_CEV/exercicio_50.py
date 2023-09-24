count = 0
soma = 0
for c in range(1,7):
    num = int(input(f'digite o {c}° valor : '))
    if num%2 == 0:
        soma += num
        count += 1
print(f'voce informou {count} pares e a soma entre eles foi {soma}')