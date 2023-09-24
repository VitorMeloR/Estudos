altura = float(input('digite a altura da sua parede: '))
largura = float(input('digite a largura da sua parede: '))
area = altura*largura
tinta = area/2
print(f'a area da sua parede é de {area:,.3f}m2')
print(f'a quantida de tinta necessária é de {tinta:,.3f}l')