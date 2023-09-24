soma=m1000=c=0
print('='*80)
print('SIMULADOR DE CAIXA M.')
print('='*80)
while True:
    nomeP = str(input('Digite o nome do produto: '))
    preçoP = float(input(f'Digite o preço do produto ({nomeP}): '))
    c+=1
    soma+=preçoP
    if preçoP > 1000:
        m1000+=1
    if c == 1:
        nomeM=nomeP
        menor=preçoP
    if preçoP < menor:
        nomeM = nomeP
        menor = preçoP
    esc = input('Deseja adicionar mais produtos [S/N]').strip().upper()[0]
    while esc not in 'SN':
        esc = input('Deseja adicionar mais produtos [S/N]').strip().upper()[0]
    print('='*80)
    if esc == 'N':
        break
print(f'O total gasto da compra foi: R${soma}')
print(f'O produto mais barato foi: {nomeM}')
print(f'{m1000} custaram mais de R$1000')