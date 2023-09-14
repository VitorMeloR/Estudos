from math import sin,cos,tan,radians
angulo = float(input('digite o angulo: '))
seno = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))
print(f'o seno do angulo:{angulo} é {seno:.2f}\no cos do angulo:{angulo} é {cos:.2f}\no tan do angulo:{angulo} è {tan:.2f}')