listfut = list()
fut = dict()
gols = list()
while True:
    fut.clear()
    fut['jogador'] = input('Qual o nome do jogador? ')
    fut['Partidas jogadas'] = int(input('Quantas partidas ele jogou? '))
    total=0
    for c in range(1,fut['Partidas jogadas']+1):
        gols.append(int(input(f'Gols na {c}º partida: ')))
    fut['total'] = sum(gols)
    listfut.append(fut.copy())
    esc = input('Deseja continuar?: ').lower().strip()[0]
    if esc == 'n':
        break
print(listfut)
print('-='*21)
print(F'{"JOGADOR":<10}{"GOLS":^15}{"TOTAL DE PARTIDAS":>10}')
for i in listfut:
    print(i)
    for n in fut.items():
        print(f'{n}')

