#81
numeros = []
c5=0
while True:
    n = int(input('digite um numero a ser adicionado: '))
    numeros.append(n)
    esc = input('deseja contiuar? [s/n]').lower()[0]
    if esc == 'n':
        break
print(f'sua lista teve {len(numeros)} ocorrencia e em ordem decrescente ficou {sorted(numeros, reverse=True)}')
for c in numeros:
    if c == 5:
        c5+=1
print(f'o numero 5 apareceu {c5} vezes' if c5 >0 else 'o 5 nao foi encontrado')