classe = dict()
classe['nome'] = input('Nome do aluno? ')
classe['nota_1'] = float(input(f'Digite a 1° nota de {classe["nome"]}: '))
classe['nota_2'] = float(input(f'Digite a 2° nota de {classe["nome"]}: '))
classe['media'] = (classe['nota_1']+classe['nota_2'])/2
if classe['media'] >= 7:
    classe['situação'] = 'Aprovado'
elif 5 <= classe['media'] < 7:
    classe['situação'] = 'Recuperação'
elif classe['media'] < 5:
    classe['situação'] = 'Reprovado'
print('-='*15)
for i,v in classe.items():
    print(f'{i:<15}',end='')
    print(f'{v:>15}',end='')
    print()