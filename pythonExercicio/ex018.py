from math import radians, sin, cos, tan

ângulo = float(input('Informe o angulo desejado: '))

seno = sin(radians(ângulo))
print('O ângulo {} tem como SENO {:.2f}.'.format(ângulo, seno))

cosseno = cos(radians(ângulo))
print('O ângulo {} tem como COSSENO {:.2f}.'.format(ângulo, cosseno))

tangente = tan(radians(ângulo))
print('O ângulo {} tem como TANGENTE {:.2f}.'.format(ângulo, tangente))