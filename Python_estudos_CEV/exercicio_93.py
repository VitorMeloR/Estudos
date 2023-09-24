fut = dict()
fut['Nome do jogador'] = input('Qual o nome do jogador? ')
partida = int(input('Quantas partidas ele jogou? '))
fut['Partidas jogadas'] = partida
total=0
for c in range(1,fut['Partidas jogadas']+1):
    fut[f'{c}º partida'] = gols = int(input(f'Gols na {c}º partida: '))
    total+=gols
fut['total'] = total
print(fut)
print('-='*20)
print(f'{"APROVEITAMENTO DE {}":^30}'.format(fut['Nome do jogador'].upper()))
for k,i in fut.items():
    print(f'{k:<17}|{i:>17}')
