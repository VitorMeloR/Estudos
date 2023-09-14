def p(titulo,nomes):
    print(f'{titulo}\n'.upper())
    for c in nomes:
        print(c,end=' | ')
    print()
    print('-='*30)


idades=list()
ficha = {'cadastro':[],'homens':[],'mulheres':[],'acima da media':[],'media':[]}
c=0
while True:
    nome=input('Digite um nome a ser cadastrado: ').strip().title()
    ficha['cadastro'].append(nome)
    while True:
        idade = input(f'Digite a idade de {ficha["cadastro"][c]}: ').strip()
        try:
            idade = int(idade)
            idades.append(idade)
            break
        except ValueError as err:
            print('Por favor digite um numero inteiro para declar a idade'.upper())
    sexo = input(f'Digite o sexo de {nome} [M/F]: ').strip().lower()[0]
    while sexo not in 'mf':
        print('ERRO OPÇÃO INVÁLIDA')
        sexo = input(f'Digite o sexo de {ficha["cadastro"][c]} [M/F]: ').strip().lower()[0]
    if sexo == 'f':
        ficha['mulheres'].append(nome)
    else:
        ficha['homens'].append(nome)
    esc = input('Deseja adicionar mais pessoas ao cadastro [S/N]').lower().strip()[0]
    while esc not in 'sn':
        print('ERRO OPÇÃO INVÁLIDA')
        esc = input('Deseja adicionar mais pessoas ao cadastro [S/N]').lower().strip()[0]
    if esc == 's':
        c+=1
    elif esc == 'n':
        break
soma = sum(idades)
ficha['media'] = media = soma/len(idades)
for i,v in enumerate(idades):
    if v > 24:
        ficha['acima da media'].append(ficha['cadastro'][i])
print('-='*30)
p('PESSOAS CADASTRADAS',ficha['cadastro'])
p('homens cadastrados',ficha['homens'])
p('mulheres castradas',ficha['mulheres'])
print('MEDIA DAS PESSOAS CADASTRDAS')
print(f"{ficha['media']:.0f}")
print('-='*30)
print('ACIMA DA MEDIA')
for c in ficha['acima da media']:
    i = ficha['acima da media'].index(c)
    print(f'{c} com {idades[i]} anos')
print('-='*30)
