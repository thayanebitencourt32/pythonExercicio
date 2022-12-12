"""
Faça um algoritmo para ler um vetor de 30 números.
Após isto, realizar a leitura de mais um número qualquer,
calcular e escrever quantas vezes esse número aparece no vetor.

"""

from exercPython2.erro import leiaInt

numeros = []


def leiaNumber():
	while True:
		try:
			for i in range(1,21):
				numero = leiaInt(f'Informe o {i} ° número:  ')
				numeros.append(numero)
			novaBusca = leiaInt('Informe um número')
			cont = 0
			for r in numeros:
				if r == novaBusca:
					cont += 1
			print(f'O número {novaBusca}, apareceu {cont} vezes.')
		except (ValueError, TypeError):
			print('\033[31m ERRO. Digite por gentileza um número válido.\033[m')
			continue
		except KeyboardInterrupt:
			print('\n\033[31m O usuário optou por sair sem digitar.\033[m')
			return 0
		else:
			return


leiaNumber()