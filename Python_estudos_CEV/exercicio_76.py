lista = ('motor 1cv', 170,
         'motor 2cv', 320,
         'motor 3cv', 450,
         'motor 4cv', 550)
print('-'*30)
print(f'{"TABELA DE PREÇOS":^30}')
print('-'*30)
for i in range(0,len(lista)):
    if i % 2 == 0:
        print(f'{lista[i]:.<30}R$'.upper(),end='')
    else:
        print(f'{lista[i]:>7}')
print('-'*30)