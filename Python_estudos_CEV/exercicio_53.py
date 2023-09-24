nome = str(input('digite uma palavra: ')).strip().upper()
palavras = nome.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print(f'A palavra {nome} é um palindromo')
else:
    print(f'A palavra {nome} não é um palindromo')
print(junto, inverso)