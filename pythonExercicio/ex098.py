from time import sleep

def contador( i, f, p):
	if p < 0:
		p *= -1
	if p==0:
		p = 1
	print(f'Contagem de {i} até {f} de {p} em {p}')

	if i < f:
		cont = i
		while cont <= f:
			print(f'{cont} ', end='', flush=True)
			sleep(0.5)
			cont += p
		print('FIM')
	else:
		cont = i
		while cont >= f:
			print(f'{cont} ', end='', flush=True)
			sleep(0.5)
			cont -= p
		print('FIM')


contador(1,10,2)
inic = int(input('Informe o inicio da contagem: '))
contag = int(input('Informe o fim da contagem: '))
passo = int(input('Informe como pretende a contagem: '))

contador(inic, contag, passo)
