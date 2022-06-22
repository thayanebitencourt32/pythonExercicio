def leiaInt(msg):
	ok = False
	valor = 0
	while True:
		n = str(input(msg))
		if n.isnumeric():
			valor = int(n)
			ok = True
		else:
			print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
		if ok:
			break
	return valor


n = leiaInt('Informe um numero: ')
print(f'Você digitou o número {n}')