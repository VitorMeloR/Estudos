deboucred = int(input('digite 1 para debito/dinheiro/pix \ndigite 2 para credito\n: '))
if deboucred == 1:
    porcento = int(input('digite o valor de desconto com compras no debito/dinheiro/pix: '))
    valor = float(input('digite o valor da compra para realizar o desconto: '))
    desconto = (valor*porcento)/100
    final = valor-desconto
    print(f'o valor do seu produto com 5% de desconto ficará em R${final:,.2f}')
else:
    print('compras com forma de pagamento no crédito não tem direito ao desconto')