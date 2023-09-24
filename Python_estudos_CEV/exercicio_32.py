salario = float(input('digite o seu salario: '))
if salario <= 1250:
    salario=(salario*15)/100+salario
    print(f'seu salario com 15% de aumeto ficou em R${salario:.2f}')
else:
    salario=(salario*10)/100+salario
    print(f'seu salario com 10% de aumento ficou em R${salario:.2f}')