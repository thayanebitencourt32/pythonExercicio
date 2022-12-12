""""
Escreva um algoritmo que permita a leitura dos nomes de 10 pessoas e armazene os nomes lidos em um vetor.
Após isto, o algoritmo deve permitir a leitura de mais 1 nome qualquer de pessoa e depois escrever a mensagem
ACHEI, se o nome estiver entre os 10 nomes lidos anteriormente (guardados no vetor), ou NÃO ACHEI caso contrário.
"""
from exercPython2.erro import leiaString

nomes = []


def leiaNomes():
	while True:
		try:
			for i in range(1,21):
				nome = leiaString(f'Informe o {i} ° nome:  ').strip().upper()
				nomes.append(nome)
			buscaPor = leiaString('Informe o nome que deseja buscar: ').strip().upper()
			for l in nomes:
				if l == buscaPor:
					print('ACHEI')
				else:
					return print('Nao achei')
		except (ValueError, TypeError):
			print('\033[31m ERRO. Digite por gentileza um número válido.\033[m')
			continue
		except KeyboardInterrupt:
			print('\n\033[31m O usuário optou por sair sem digitar.\033[m')
			return 0
		else:
			return


leiaNomes()
