def aumentar(preco = 0 , taxa = 0, format=False):
	res = preco + (preco * taxa/100)
	return res if format is False else moeda(res)


def diminuir(preco = 0, taxa = 0,format=False):
	res = preco - (preco * taxa/100)
	return res if format is False else moeda(res)


def dobro(preco = 0,format=False):
	res = preco * 2
	return res if not format else moeda(res)


def metade(preco = 0 , format=False):
	res = preco / 2
	return res if format is False else moeda(res)


def moeda(preco = 0, moeda = 'R$'):
	return f'{moeda}{preco:.2f}'.replace('.',',')

def resumo(preco = 0, taxaa=10, taxar=5):
	print('-'*30)
	print('RESUMO DO VALOR'.center(30))
	print('-'*30)
	print(f'Preco analisado: \t{moeda(preco)}')
	print(f'Dobro do preço: \t{dobro(preco, True)}')
	print(f'Diminuindo {taxar}%: \t{diminuir(preco, 10,True)}')
	print(f'Metade do preço: \t{metade(preco, True)}')
	print(f'Aumentando {taxaa}%: \t{aumentar(preco, 10,True)}')
	print('-'*30)


