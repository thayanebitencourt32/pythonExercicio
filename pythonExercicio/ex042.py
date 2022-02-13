print('*-*-*'*12)
print('    ANALISANDO SE PODE FORMAR TRIÂNGULO E TIPO')
print('*-*-*'*12)
seg1 = float(input('Informe o primeiro segmento: '))
seg2 =  float(input('Informe o segundo segmento: '))
seg3 = float(input('Informe o terceiro segmento: '))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Os segmentos podem formar  um TRIÂNGULO: ')
    if seg1 == seg2 and seg2 == seg3: # seg1 == seg2 == seg3
        print('EQUILÁTERO.')
    elif seg1 != seg2 != seg3 != seg1:
        print('ESCALENO.')
    else:
        print('ISÓSCELES.')
else:
    print('Os segmentos não podem formar TRIÂNGULO.')