from datetime import datetime
ficha = dict()
ficha['nome'] = input('Digite o nome do cidadão: ').title().strip()
idade = int(input(f'Digite o ano nascimento do {ficha["nome"]}: '))
ficha['idade'] = datetime.now().year-idade
ficha['ctps'] = int(input(f'Digite o numéro da CTPS de {ficha["nome"]} (0 caso não tenha): '))
if ficha['ctps'] > 0:
    ficha['contratação'] = int(input('Digite o ano de contração: '))
    ficha['salario'] = float(input('Digite o salário: '))
    ficha['aposentado'] = ficha['idade']+((ficha['contratação']+35) - datetime.now().year)
    print('-='*15)
    print(f'     FICHA DE {ficha["nome"].upper()}')
    for k,v in ficha.items():
        print(f'{k:<15}|{v:>15}')
    print('-=' * 15)
else:
    print('-=' * 15)
    print(f'         FICHA DE {ficha["nome"].upper()}')
    for k, v in ficha.items():
        print(f'{k:<15}|{v:>15}')
    print('-=' * 15)