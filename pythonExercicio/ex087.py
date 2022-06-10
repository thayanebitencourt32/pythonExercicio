matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = somaterceira = mai = 0
# PROGRAMA QUE CRIA MATRIZ DE ORDEM 3
for l in range(0, 3):
	for c in range(0, 3):
		matriz[l][c] = int(input(f'Informe o valor para posição [{l}, {c}] '))

for l in range(0, 3):
	for c in range(0, 3):
		print(f'[{matriz[l][c]:^5}]', end='')
		if matriz[l][c] % 2 == 0:
			somapar += matriz[l][c]
	print()
for l in range(0, 3):
	somaterceira += matriz[l][2]
for c in range(0, 3):
	if c == 0:
		mai = matriz[1][c]
	elif matriz[1][c] > mai:
		mai = matriz[1][c]

print(f'A soma dos pares foi {somapar}')
print()
print(f'A soma dos valores da terceira coluna foi {somaterceira}')
print()
print(f'O maior valor da segunda linha foi: {mai}')
