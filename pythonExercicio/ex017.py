from math import hypot
co = float(input('Medida do cateto oposto:  '))
ca = float(input('Medida do cateto adjacente:  '))

hi = hypot(co, ca)

print('A hipotenusa é: {:.2f}'.format(hi))