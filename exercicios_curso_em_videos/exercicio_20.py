from random import shuffle
nome = []
while True:
    n = int(input('quantos itens serão embaralhados? '))
    for n in range(n):
        nomes = str(input(f'digite o {n+1}° iten: '))
        nome.append(nomes)
    shuffle(nome)
    print(f'a ordem da lista ficou {nome}')
    print('=' * 30)
    menu = input('digite 1 para finalizar o serteio e 2 para continuar: ')
    if menu == '1':
        break
fim = 'fim'
print(f'{fim:=^80}')
