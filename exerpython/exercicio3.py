"""
Ler 2 números de um alunos.
Calcular a média e exibir se o aluno foi aprovado ou reprovado ou aonde se está de exame.
Se a média for maior ou igual a 6,0 o aluno estará aprovado,
caso contrário se a média for igual a 4,0 mas menor que 6,0 então o aluno estará de exame.
Caso contrário estará reprovado.
"""
from exerpython.erro import leiaString, leiaFloat

notas = []
nome = []


def nome():
	total = media = 0
	nome = leiaString('Informe o nome do aluno:  ')
	for i in range(1,3):
		nota = leiaFloat(f'Informe a {i}º nota, de {nome}:  ')
		notas.append(nota)
	media = (notas[0] + notas[1]) / 2
	if media > 6.0:
		print(f'O aluno {nome} foi aprovado, média {media}')
	else:
		print(f'O alunoo {nome} foi reprovado, média {media}.')
	return
nome()
