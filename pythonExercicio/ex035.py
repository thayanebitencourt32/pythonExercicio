print('*****--- IDENTIFICANDO SE PODE OU NÃO FORMAR TRIÂNGULO---*****')

r1 = float(input('Informe primeiro segmento: '))
r2 = float(input('Informe segundo segmento: '))
r3 = float(input('Informe terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 +r2:
    print ('Os segmentos podem formar triângulo.')
else:
    print ('Os segmentos não podem formar triângulo.')