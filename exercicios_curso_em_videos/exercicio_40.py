media1 = float(input('digite uma primeira nota: '))
media2 = float(input('digite uma segunda nota: '))
media3 =float(input('digite uma terceira nota: '))
mediaf =( media1+media2+media3)/3
if mediaf < 5.0:
    print('voce foi reprovado')
if mediaf >= 5 and mediaf <= 6.9:
    print('voce esta de recuperação')
if mediaf >= 7.0:
    print('voce foi aprovado')