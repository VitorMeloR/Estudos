salario = float(input('digite o salario do funcionario: R$'))
aumento = (salario*15)/100
aumento = aumento+salario
print(f'seu salario com 15% de aumento ficara em R${aumento:,.2f}')