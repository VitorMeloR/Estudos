frase = str(input('digite uma frase: ')).strip().upper()
print(f'a letra A aparece {frase.count("A")} vezes nessa frase')
print(f'a primeira letra A aparecu na posição {frase.find("A")+1}')
print(f'a ultima letra apareceu na posição {frase.rfind("A")}')
