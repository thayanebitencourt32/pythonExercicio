from time import sleep
from pythonExercicio.ex115.lib.arquivo import *
from pythonExercicio.ex115.lib.interface import *

arq = "meunovoarquivo.txt"

if not arquivoExiste(arq):
	criarArquivo(arq)

while True:
	resposta = menu(['Pessoas cadastradas','Cadastrar novo', 'Sair '])
	if resposta == 1:
		#opção de ler arquivo
		lerArquivo(arq)
	elif resposta == 2:
		cabecalho('Novo Cadastro')
		nome = str(input('Nome: '))
		idade = leiaInt('Idade: ')
		cadastrar(arq, nome, idade)
	elif resposta == 3:
		cabecalho('Sair do sistema')
		break
	else:
		print('Informe uma opção válida')
	sleep(2)