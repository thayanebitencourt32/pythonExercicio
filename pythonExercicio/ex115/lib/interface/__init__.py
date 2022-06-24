def leiaInt(msg):
	while True:
		try:
			n = int(input(msg))
		except (ValueError,TypeError):
			print('\033[31m ERRO. Digite por gentileza um número inteiro válido.\033[m')
			continue
		except(KeyboardInterrupt):
			print('\n\033[31m O usuário optou por sair sem digitar.\033[m')
			return 0
		else:
			return n


def linha(tam = 42):
	return '-' * tam


def cabecalho(txt):
	print(linha())
	print(txt.center(42))
	print(linha())


def menu(lista):
	cabecalho('\033[31mMENU\033[m')
	c = 1
	for item in lista:
		print(f'{c} - {item}')
		c += 1
	print(linha())
	opc = leiaInt('Opção: ')
	return opc


