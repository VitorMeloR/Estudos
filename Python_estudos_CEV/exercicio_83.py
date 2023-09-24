c=0
expressao = str(input('digite uma expressão: '))
for lista in expressao:
    if lista == '(' or lista == ')':
        c+=1

if c%2 == 0:
    print('Sua expressão é valida')
elif c%2 == 1 or expressao[0] == ')' and expressao[-1] == '(':
    print('Sua expressão é invalida')