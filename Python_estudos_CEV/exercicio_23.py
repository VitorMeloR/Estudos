print('inicando contagem de casas decimais')
while True:
    num = int(input('digite um numero: '))
    print(f'analisando o numero {num}')
    u = num//1%10
    d = num//10%10
    c = num//100%10
    m = num//1000%10
    print(f'o numero {num} tem:\n{u} unidades\n{d} dezenas\n{c} centenas\n{m} milhares')
    print('-'*80)
    esc = input('deseja terminar o programa? [s/n]').strip().lower()
    if esc == 's':
        break
print(f'{"fim do programa":-^80}')
