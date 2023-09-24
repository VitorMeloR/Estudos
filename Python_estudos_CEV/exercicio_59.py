from time import sleep
valor1 = int(input('digite o primeiro valor: '))
valor2 = int(input('digite o segundo valor: '))
escolha = ''
while not escolha == '5':
    sleep(2)
    print('=-'*15)
    print('     [ 1 ] somar\n     [ 2 ] multiplicar\n     [ 3 ] maior\n     [ 4 ] novos números\n     [ 5 ] sair do programa')
    print('=-' * 15)
    escolha = str(input('ESCOLHA UMA OPÇÃO: '))
    print('=-' * 15)
    if escolha == 1:
        resultado = valor1 + valor2
        print(f'O RESULTADO DESSA SOMA: {valor1}+{valor2}={resultado}')
    if escolha == 2:
        resultado = valor1*valor2
        print(f'O RESULTADO DESSA MULTILIÇÃO: {valor1}x{valor2}={resultado}')
    if escolha == 3:
        if valor1 > valor2:
            print(f'O {valor1} é maior que o {valor2}')
        else:
            print(f'O {valor2} é maior que o {valor1}')
    if escolha == 4:
        print('Tudo bem digite os novo numeros')
        valor1 = int(input('digite o primeiro valor: '))
        valor2 = int(input('digite o segundo valor: '))
    if escolha == 5:
        escolha = 5