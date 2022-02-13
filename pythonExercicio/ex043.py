print('*-*-*-*'*5)
print(' Calculando massa corporal - IMC ' )
print('*-*-*-*'*5)

peso = float(input('Informe o peso:kg  '))
altura = float(input('Informe sua altura:m  '))

imc = peso / (altura ** 2)

print('O seu IMC é {:.1f}.'.format(imc))

if imc < 18.5 :
  print('Você está abaixo do peso')
elif 18.5 <= imc < 25:
  print('PARABÉNS, peso ideal')
elif 25 <= imc < 30:
  print('Você está com SOBREPESO')
elif 30 <= imc < 40:
  print('Você esta com OBESIDADE')
else:
  print('Cuidado, você está com obesidade MÓRBIDA')