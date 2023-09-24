cadastro = [[],[]] #inicio uma lista dupla
print('-='*15)
print(f'{"CADASTRO DE PESSOAS":^30}')
print('-='*15)
print(f'{"NOMES":^30}')
while True: #cadastro dos nomes na primeira lista
    cadastro[0].append(input('Digite o nome a ser cadastrado: ').strip().capitalize())
    esc = input('Deseja consitnuar? [s/n]: ').lower().strip()[0]
    while esc not in 'sn': #testo se a opção digitada é valida
        print('Opção invalida tente novamente')
        esc = input('Deseja consitnuar? [s/n]: ').lower().strip()[0]
    if esc == 'n': #termina o cadastro de pessoas
        break
print('-='*15)
print(f'{"PESOS":^30}')
for i,v in enumerate(cadastro[0]):
    while True: #cadastro o peso de cada pessoa
        peso = input(f'Digite o peso de {v}: ').replace(',','.').strip()
        try: #verifico se o peso foi digitado de forma correta
            peso = float(peso)
            break
        except ValueError as err:
            print('Favor, digite um numero')
    cadastro[1].append(peso) #adiciono o peso na segunda lista
print('-='*15)
print(f'{"PESSOAS CADASTRADAS":^30}')
for i,v in enumerate(cadastro[0]): #mostro de forma organizada a lista
    print(f'nome: {v:<10}',end=' | ')
    while True:
        print(f'peso: {cadastro[1][i]:>}Kg')
        break
print('-='*15)
for i,v in enumerate(cadastro[1]): #testo e mostro quem está acima do peso
    if i == 0 and v > 70:
        print(f'{"ACIMA DO PESO":^30}')
        print('-=' * 15)
    if v > 70:
        print(f'{cadastro[0][i]} com {v}KG\n')
for i, v in enumerate(cadastro[1]): #testo e mostro quem está abaixo do peso
    if i == 0 and v < 50:
        print(f'{"ABAIXO DO PESO":^30}')
        print('-=' * 15)
    if v < 50:
        print(f'{cadastro[0][i]} com {v}KG\n')

