from colorama import init, Fore, Back
import numpy as np
escolhidos = []
numeros = []


def leiaInt(msg):
	try:
		n = int(input(msg))
	except (ValueError, TypeError):
		print('\033[31m ERRO. Digite por gentileza um número inteiro válido.\033[m')
	except(KeyboardInterrupt):
		print('\n\033[31m O usuário optou por sair sem digitar.\033[m')
		exit()
	return n


def linha(tam=42):
	return '-' * tam


def cabecalho(txt):
	print(linha())
	print(txt.center(42))
	print(linha())


def menu(lista):
	cabecalho('\033[31mBEM VINDO AO POOCOBUS!\033[m')
	c = 1
	for item in lista:
		print(f'{c} - {item}')
		c += 1
	print(linha())


def obter_disponiveis():
	lista = list(dict.fromkeys(numeros))
	for escolhido in escolhidos:
		lista.remove(escolhido)
	return lista


def escolhaAssentos(msg):
	global numer
	try:
		matriz()
		escolha = int(input(msg))
		matriz()
		while escolha not in numeros or escolha in escolhidos:
			print('Não é possível efetuar a reserva, verifique se a escolha está disponível(verde).')
			escolha = int(input(msg))
		escolhidos.append(escolha)
		numeros.remove(escolha)
		print(numeros)
		print(escolhidos)
		print(f'Passagem: {escolha} reservada(as). ')
		matriz()
		return escolhidos
	except(ValueError, TypeError):
		print('\033[31m ERRO. Digite por gentileza um número inteiro válido.\033[m')
		return
	except(KeyboardInterrupt):
		print('\n\033[31m O usuário optou por sair sem digitar.\033[m')
		exit()


def matriz():
	init(autoreset=True)

	linha = 8
	coluna = 5
	mat = np.zeros([linha, coluna], dtype=int)  # para criar matriz com numeros inteiros
	numero = 1

	for l in range(linha):
		for c in range(coluna):
			if l == 0 and c == 0:  # é o motorista
				mat[l, c] = 0
				print(f'{Back.BLUE}{Fore.BLACK} {mat[l, c]:^3}', end=' ')
			elif c == 2 or l == 0:  # é o corredor
				mat[l, c] = 0
				print(f'{Back.WHITE}{Fore.BLACK} {mat[l, c]:^3}', end=' ')
			else:
				mat[l, c] = numero
				if numero in escolhidos:
					print(f'{Back.RED}{Fore.BLACK} {mat[l, c]:^3}', end=' ')
				else:
					print(f'{Back.GREEN}{Fore.BLACK} {mat[l, c]:^3}', end=' ')
					numeros.append(numero)
				numero += 1

		print('')
		print('')
