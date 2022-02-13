num1 = int(input('Informe um número: '))
num2 = int(input('Informe outro número: '))

if num1 > num2:
    print('O primeiro número é maior que o segundo. {} > {}.'.format(num1, num2))
elif num1 < num2:
    print('O segundo número é maior que o primeiro. {} > {}.'.format(num2, num1))
else:
    print('Não existe valor maior, os dois são iguais.')