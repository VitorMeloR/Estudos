from random import choice
from time import sleep
#\033[0:32m verde
#\033[0:31m vermelho
#\033[0:36m azul
print('\033[0:36m=-'*100)
print('Vamos jogar pedra, papel ou tesoura!!!')
print('=-'*100)
while True:
    escolha = str(input('Diga a sua escolha: '
                        '[p = palpel]'
                        '[pd = pedra]'
                        '[t = tesoura]: \033[m'))
    jogo = ['p','t','pd']
    jogo = choice(jogo)
    if jogo == escolha:
        print('empate')
    if jogo == 'pd' and escolha == 't':
        print('eu ganhei hahaha!!')
    if jogo == 'p' and escolha == 'pd':
        print('eu ganhei hahaha!!')
    if jogo == 't' and escolha == 'p':
        print('eu ganhei hahaha!!')
    if jogo == 't' and escolha == 'pd':
        print('droga você ganhou')
    if jogo == 'pd' and escolha == 'p':
        print('droga você ganhou')
    if jogo == 'p' and escolha == 't':
        print('droga você ganhou')
    sn = str(input('deseja continuar?[s/n]:'))
    if sn == 'n':
        break