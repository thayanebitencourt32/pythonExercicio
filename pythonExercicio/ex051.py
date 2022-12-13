print('*-*-*'*15)
print('PROGRAMA PARA MOSTRAR 10 PRIMEIROS PA')
print('*-*-*'*15)

numberone = int(input('Informe primeiro número:  '))
razao = int(input('Informe a razão: '))
decimo = numberone + (10-1)* razao

for c in range(numberone, decimo + razao, razao):
      print('{}' .format(c) , end = '• ')
print('ACABOU!')