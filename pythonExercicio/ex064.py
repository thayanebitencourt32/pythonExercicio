num = int(input('Informe  um numero: [999 para parar]'))
cont  = 0
soma = 0
while num != 999:
    cont += 1
    soma += num
    num = int(input('Informe um número: [digite 999 para parar]'))

print('Você digitou {} números e a soma entre eles foi {}.'.format(cont,soma))