def nota(*n, sit=False):
	"""
	analisa nota e situação de aluno
	:param n: umaou mais nota
	:param sit: opcional se deve ou não adcionar situação
	:return: varias inf do dicionario sobre situacao da turma
	"""
	r=dict()
	r['total'] = len(n)
	r['maior'] = max(n)
	r['menor'] = min(n)
	r['media'] = sum(n)/len(n)
	if sit:
		if r['media'] >= 7:
			r['situacao'] = 'BOA'
		elif r['media'] >= 5:
			r['situacao'] = 'RAZOÁVEL'
		else:
			r['situacao'] = 'RUIM'
	return r


resp = nota(5.5 , 2.5 , 1.5 ,sit=True)
print(resp)
help(nota)

