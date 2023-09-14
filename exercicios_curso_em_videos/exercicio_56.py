
media = 0
maior = 0
m20 = 0
nomev = ''
for a in range(1,5):
    print(f'-------------------------{a}° PESSOA-------------------------')
    nome = str(input(f'digite o nome da {a}° pessoa : '))
    idade = int(input(f'digite a idade do(a) {nome} : '))
    sexo = str(input(f'digite o sexo do(a) {nome}: [m/f] ')).strip().lower()
    media += idade
    if a == 1 and sexo == 'm':
        maior = idade
    else:
        if idade > maior and sexo == 'm':
            maior = idade
            nomev = nome
    if idade < 20 and sexo == 'f':
        m20+=1
media = media/4
print(f'A média de idade dessa 4 pessoas é de {media:.0f} anos')
print(f'O homem mais velho é {nomev} e tem {maior} anos')
print(f'E tem {m20} mulheres com menos de 20 anos')