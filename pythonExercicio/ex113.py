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


def leiaFloat(msg):
	while True:
		try:
			n = float(input(msg))
		except(ValueError, TypeError):
			print('\033[31m ERRO. Digite um número valido.\033[m')
			continue
		except(KeyboardInterrupt):
			print('\033[31m Usuário optou por sair. \033[m')
			return 0
		else:
			return n

num1 = leiaInt('Digite um Inteiro: ')
num2 = leiaFloat('Digite um número real: ')
print(f'Os valores digitados foram: {num1} e {num2}')
