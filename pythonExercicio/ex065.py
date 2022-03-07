print('Menor e maior numero e media entre eles')
media = cont = quant = 0
resp = 'S'
while resp in 'Ss':
    num1 = int(input('Digite um numero: '))
    cont += num1
    quant += 1
    if quant == 1:
        maior = menor = num1
    else:
        if num1 > maior:
            maior = num1
        if num1 < menor:
            menor = num1
    resp = str(input('Quer continuar? [s/n]')).upper().strip()[0]
media = cont /quant
print('Você digitou {}números e a média foi {}'.format(quant, media))
print('O maior valor foi {} e o menor valor {}.'.format(maior,menor))