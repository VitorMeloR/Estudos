#80
lista_n=[]
c=0
while c != 5:
    n = int(input('digite um numero: '))
    if n not in lista_n:
        lista_n.append(n)
        c+=1
    else:
         print('numero ja adicionado, tente de novo')
ordem=[]
ordem.insert(0,min(lista_n))
ordem.insert(4,max(lista_n))
lista_n.remove(max(lista_n))
lista_n.remove(min(lista_n))
ordem.insert(1,min(lista_n))
ordem.insert(2,max(lista_n))
ordem.insert(2,lista_n[1])
print(f'sua lista em ordem:')
print(ordem)