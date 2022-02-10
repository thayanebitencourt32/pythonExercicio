num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe segundo número: '))
num3 = int(input('Informe terceiro número: '))
menor = num1
if num2 < num1 and num2<num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print('O menor valor digitado foi: {}'.format(menor))
print('O maior valor digitado foi: {}'.format(maior))