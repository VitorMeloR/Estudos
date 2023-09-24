print('='*50)
print('CADASTRO DE PESSOAS')
print('='*50)
c=0
menor_20=0
maior_18=0
homens=0
while True:
    nome = input('digite o nome a ser cadastrado: ').strip()
    idade = int(input(f'digite a idade de {nome}: '))
    sexo = input(f'digite o sexo de {nome} [M/F]').strip().upper()[0]
    while sexo not in 'MF':
         sexo = str(input(f'digite o sexo de {nome} [M/F]')).strip().upper()[0]
    c+=1
    if idade > 18:
        maior_18+=1
    if sexo == 'M':
        homens+=1
    if sexo == 'F' and idade < 20:
             menor_20+=1
    esc = input('deseja adicionar algum cadastro? [S/N]: ').strip().upper()[0]
    while esc not in 'SN':
             esc = input('deseja adicionar algum cadastro? [S/N]: ').strip().upper()[0]
    if esc == 'N':
        break
print(f'Você cadastrou {c} pessoas\nTem {menor_20} mulheres menores de 20 anos\nForam cadastrados {homens} homens no sistema\nE tem {maior_18} maiores de 18 anos')