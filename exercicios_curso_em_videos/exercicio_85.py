#85
lista=[]
par = []
impar = []
while True:
    lista.append(int(input('digite um valor a ser adicionado: ')))
    esc = input('deseja continuar [s/n]: ')
    if esc[0] in 'Nn':
        break
for c in lista:
    if c%2 == 0:
        par.append(c)
    else:
        impar.append(c)
print(f'Sua lista ficou: {sorted(lista)}')
print(f'os numeros pares são {sorted(par)}')
print(f'os impares são {sorted(impar)}')