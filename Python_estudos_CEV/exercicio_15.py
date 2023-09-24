dia = int(input('quantos dias alugados: '))
km = float(input('quantos km rodasos: '))
valor =(dia*60)+(km*0.15)
print(f'valor total a pagar do aluguel do carrro é de R${valor:,.2f}')