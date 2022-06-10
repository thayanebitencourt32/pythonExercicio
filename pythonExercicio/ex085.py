valor = list()

pares = list()
impar = list()
for c in range(1,8):
    valor.append(int(input(f'Digite o {c}º valor: ')))

for i, v in enumerate(valor):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impar.append(v)
pares.sort()
print(f'A lista completa dos pares é: {pares}')
impar.sort()
print(f'A lista completa dos impares é: {impar}')

#de Guanabara

num= [[],[] ]
valor = 0
for c in range(1,8):
	valor = int(input(f'Digite o {c}º valor '))
	if valor % 2 == 0:
		num[0].append(valor)
	else:
		num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'Os valores pares são: {num[0]}')
print(f'Os valores impares são:{num[1]}')