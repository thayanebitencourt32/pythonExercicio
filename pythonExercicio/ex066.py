num1 = int(input('Informe um número: [999 faz parar]'))

cont = quant = 0

while num1 != 999:'while True'
    cont += 1
    quant= num1 + quant
    num1 = int(input('Informe um número: [999 faz parar]'))
    if num1 == 999:
        break

print(f'Você digitou {cont} números e a soma deles foi {quant}')
