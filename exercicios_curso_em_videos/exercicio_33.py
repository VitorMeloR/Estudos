num1 = int(input('digite um valor: '))
num2 = int(input('digite um segundo valor: '))
num3= int(input('digite um terceiro valor: '))
if num1 > num2 and num1 > num3:
    print(f'o {num1} é maior')
if num2 > num1 and num2 > num3:
    print(f'o {num2} é maior')
if num3 > num1 and num3 > num2:
    print(f'o {num3} é maior')
if num1 < num2 and num1 <  num3:
    print(f'o {num1} é menor')
if num2 < num1 and num2 < num3:
    print(f'o {num2} é menor')
if num3 < num1 and num3 < num2:
    print(f'o {num3} é menor')