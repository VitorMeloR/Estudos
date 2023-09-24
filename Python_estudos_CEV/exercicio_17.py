from math import pow,sqrt
oposto_b = float(input('digite o cateto oposto: '))
adjacente_c = float(input('digite o cateto adjacente: '))
hipotenusa = oposto_b.__pow__(2)+adjacente_c.__pow__(2)
hipotenusa = sqrt(hipotenusa)
print(f'a hipotenusa dos catetos é {hipotenusa:.1f}')