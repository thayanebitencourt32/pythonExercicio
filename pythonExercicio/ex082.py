valor = list()
pares = list()
impar = list()
while True :
    valor.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar? [S/N]'))
    if resp in 'Nn':
        break
print(valor)

for i, v in enumerate(valor):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impar.append(v)
print(f'A lista completa é: {valor}')
print(f'A lista completa dos pares é: {pares}')
print(f'A lista completa dos impares é: {impar}')