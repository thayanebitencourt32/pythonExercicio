""""
Escreva um algoritmo que permita a leitura das notas de uma turma de 20 alunos.
Calcule a média da turma, conte quantos alunos obtiveram nota acima desta média calculada.
Exiba a média da turma e o resultado da contagem
"""
from exercPython2.erro import leiaFloat

notas = []
somaNotas = 0


def leiaNotas():
	while True:
		try:
			for i in range(1,21):
				nota = leiaFloat(f'Informe o {i} ° nota:  ')
				while nota > 10:
					print("Não validado.")
					nota = leiaFloat(f'Informe o {i} ° nota:  ')
				notas.append(nota)
			somaNotas = 0
			for valor in notas:
				somaNotas += valor
			media = ((somaNotas)/i)
			cont = 0
			for r in notas:
				if r > media:
					cont += 1
			print(f'A média dos {i} alunos foi de {media}')
			print(f'{cont} alunos, obteve(iveram) nota(as) acima da média')
		except (ValueError, TypeError):
			print('\033[31m ERRO. Digite por gentileza um número válido.\033[m')
			continue
		except KeyboardInterrupt:
			print('\n\033[31m O usuário optou por sair sem digitar.\033[m')
			return 0
		else:
			return nota


leiaNotas()



