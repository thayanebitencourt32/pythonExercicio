from pocobus01.lab01.interface.interface import cabecalho


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
         #dado[1] = dado[1].replace('\n', '')
         print(f'O cliente {dado[0]:<8} reservou {dado[1]:<4} passagem.Reservados {dado[2]:<6} Assentos disponiveis {dado[3]:<30}')
      print(a.readlines())


def cadastrar(arq, nome='desconhecido',qtd=0,escolha=[],disponiveis=[]):
	try:
		a = open(arq,'at')
	except:
		print('Houve um erro na abertura do consulta')
	else:
		try:
			a.write(f'{nome};{qtd};{escolha};{disponiveis}\n')
		except:
			print('Houve erro')
		else:
			print(f'Compra de {nome} foi realizado.')
			a.close()

