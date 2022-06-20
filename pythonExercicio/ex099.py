from time import sleep

def maior(*num):
	cont = maior = 0
	print('-=-'*30)
	print('Analisando os valores passados...')
	for valor in num:
		print(f'{valor}', end=' ', flush=True)
		sleep(0.6)
		if cont == 0:
			maior = valor
		else:
			if valor > maior:
				maior = valor
		cont += 1
	print(f'Foram informados {cont} números.')
	print(f'O maior número informado foi: {maior}')


maior(0,9,8,4)
maior(2,3,8,5,4)
maior(0,9)