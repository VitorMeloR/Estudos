from random import randint
from time import sleep
from operator import itemgetter
dados = dict()
dados['jogador_vitor'] = randint(1,6)
dados['jogador_brenda'] = randint(1,6)
dados['jogador_isaque'] = randint(1,6)
dados['jogador_lucas'] = randint(1,6)
ranking = list()
print('-='*15)
print(f"{'JOGO':^30}")
for jog,num in dados.items():
    print(f'{jog} tirou {num} no dado.')
    sleep(1)
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
print('-='*15)
print(f"{'RANKING':^30}")
for i,v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
print('-='*15)