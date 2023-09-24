from random import choices
nome = []
while True:
    n = int(input('quantos nomes serão sorteados? '))
    for n in range(n):
        nomes = str(input(f'digite o {n+1}° nome: '))
        nome.append(nomes)
    sorteado = choices(nome)
    print(f'o nome sorteado foi {sorteado}')
    print('=' * 30)
    menu = input('digite 1 para finalizar o serteio e 2 para continuar: ')
    if menu == '1':
        break
print(f'{"fim":=^80}')
