def area(larg, comp):
	total = larg * comp
	print(f'A área para as medidas: largura {larg} e comprimento {comp}, é de : {total} m ')


print('Cálculo de terreno')
l = float(input('Largura(m):  '))
c = float(input('Comprimento(m): '))
area(l, c)