aluno = dict()

aluno['nome'] = str(input('Nome do Aluno: '))
aluno['media'] = float(input(f'Média do Aluno {aluno["nome"]}: '))
if aluno['media'] >= 7:
	aluno['situacao'] = 'Aprovado '
elif 5 <= aluno['media'] < 7:
	aluno['situacao'] = 'Recuperação '
else:
	aluno['situacao'] = 'Reprovado '

for k,v in aluno.items():
	print(f'{k} é igual a {v}')