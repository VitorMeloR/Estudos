count=0
soma=0
while True:
    n = int(input('digite um numero: '))
    soma+=n
    count+=1
    if count == 1:
            maior = n
            menor =n
    else:
        if n > maior:
            maior =n
        if n< menor:
            menor =n
    esc = input('deseja continuar [s/n]')
    if esc == 'n':
        break
media=soma/count
print(f'a media desses {count} é de {media}\nO maior numero digitado foi {maior}\nO menor numero digitado foi {menor}')