""""
Faça um algoritmo para ler 20 números e os armazene em um vetor.
 Após a leitura total dos 20 números, o algoritmo deve escrever esses 20 números lidos na ordem inversa.
"""
from exercPython2.erro import leiaInt

numeros = []


def leiaNumeros():
	while True:
		try:
			for i in range(1,21):
				numero = leiaInt(f'Informe o {i} ° número:  ')
				numeros.append(numero)
			numeros.reverse()
			print(f'Os números lidos na ordem inversa:{numeros}')
		except (ValueError, TypeError):
			print('\033[31m ERRO. Digite por gentileza um número válido.\033[m')
			continue
		except KeyboardInterrupt:
			print('\n\033[31m O usuário optou por sair sem digitar.\033[m')
			return 0
		else:
			return


leiaNumeros()