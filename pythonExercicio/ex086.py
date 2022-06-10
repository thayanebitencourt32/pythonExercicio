matriz = [[0,0,0],[0,0,0],[0,0,0]]
#PROGRAMA QUE CRIA MATRIZ DE ORDEM 3
for l in range(0,3):
	for c in range(0,3):
		matriz[l][c] = int(input(f'Informe o valor para posição [{l}, {c}] '))
for l in range(0,3):
	for c in range(0,3):
		print(f'[{matriz[l][c]:^5}]',end='')
	print()