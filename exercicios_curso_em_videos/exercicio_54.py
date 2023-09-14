count = 0
count2 = 0
for n in range(1,8):
    idade = int(input(f'digite o ano de nascimento da {n}° pessoa: '))
    idade = 2023-idade
    if idade >= 18:
        count+=1
    if idade < 18:
        count2+=1
print(f'{count} são maior de idade e {count2} são menores de idade')

