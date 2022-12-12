from pythonExercicio.ex115.lib.interface import *


def arquivoExiste(nome):
	try:
		a = open(nome, 'rt')
		a.close()
	except FileNotFoundError:
		return False
	else:
		return True


def criarArquivo(nome):
	try:
		a = open(nome, 'wt+')
		a.close()
	except:
		print('Houve um Erro na criação')
	else:
		print(f'Arquivo {nome} foi criado')


def lerArquivo(nome):
	try:
		a = open(nome, 'rt')
	except:
		print('Erro ao ler consulta')
	else:
		cabecalho('Pessoas cadastradas')
		for linha in a:
			dado = linha.split(';')
			dado[1] = dado[1].replace('\n', '')
			print(f'{dado[0]:<30}{dado[1]:>3}anos')
		print(a.readlines())


def cadastrar(arq, nome='desconhecido', idade=0):
	try:
		a = open(arq,'at')
	except:
		print('Houve um erro na abertura do consulta')
	else:
		try:
			a.write(f'{nome};{idade}\n')
		except:
			print('Houve erro')
		else:
			print(f'Cadastro de {nome} foi realizado.')
			a.close()