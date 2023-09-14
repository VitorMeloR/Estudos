moeda = int(input('digite 1 para converter real em dolar \ndigite 2 para converter dolar em real\n:'))
if moeda == 1:
    valor = float(input('digite quantos reais tem na sua carteira: '))
    dolar = valor*0.20
    print(f'seu dinheiro convertido em dolares é: US{dolar:,.2f}')
if moeda == 2:
    valor = float(input('digite quantos dolares você tem na sua carteira: '))
    real = valor*4.90
    print(f'seu dinheiro convertido em real é: R${real:,.2f}')
