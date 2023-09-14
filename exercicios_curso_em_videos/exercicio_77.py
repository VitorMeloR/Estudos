palavras = ('eu', 'sou','gostoso','demais')
for p in palavras:
    print(f'\nNa palavra {p} temos',end='')
    for letra in p:
        if letra in 'aiuo':
            print(f' ({letra})',end='')
    print(' como vogal')

