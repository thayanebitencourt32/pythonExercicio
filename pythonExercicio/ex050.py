soma  = 0
cont = 0

for c in range(1,7):
    num=int(input('Informe o {}  número:  '.format(c)))
    if num % 2 == 0:
        soma += num
        cont +=1
print('Você informou {} números PARES e a SOMA foi {}.'.format(cont, soma))