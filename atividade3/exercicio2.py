"""
A nota final de uma determinada disciplina do curso de Administração é calculada a partir de 3 notas atribuídas,
respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final.
 As notas variam de 0 a 10, sendo que a média final é a média ponderada das três notas mencionadas anteriormente.
 A tabela a seguir fornece o peso de cada nota:
Faça um programa que leia as três notas de um determinado aluno, calcule a média ponderada e escreva o conceito final
 do aluno, baseado na seguinte tabela:

"""

from exercPython2.erro import leiaFloat

notas = []
somaNotas = n1 = n2 = n3 = 0


def leiaNotas():
	while True:
		try:
			for i in range(1,4):
				nota = leiaFloat(f'Informe o {i} ° nota:  ')
				while nota > 10:
					print("Não validado.")
					nota = leiaFloat(f'Informe o {i} ° nota:  ')
				notas.append(nota)
				if i == 1:
					n1 = nota*2
				if i == 2:
					n2 = nota*3
				if i == 3:
					n3 = nota*5
			somaNotas = (n1 + n2+ n3)/10
			if somaNotas > 8:
				print(f'Conceito A, media  {somaNotas}')
			if somaNotas < 8 and somaNotas > 7:
				print(f'Conceito B, media  {somaNotas}')
			if somaNotas < 7 and somaNotas > 6:
				print(f'Conceito C, media  {somaNotas}')
			if somaNotas < 6 and somaNotas > 5:
				print(f'Conceito D, media  {somaNotas}')
			if somaNotas < 5:
				print(f'Conceito E, media  {somaNotas}')
		except (ValueError, TypeError):
			print('\033[31m ERRO. Digite por gentileza um número válido.\033[m')
			continue
		except KeyboardInterrupt:
			print('\n\033[31m O usuário optou por sair sem digitar.\033[m')
			return 0
		else:
			return nota


leiaNotas()