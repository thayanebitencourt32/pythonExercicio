from time import sleep
from pocobus01.lab01.interface.interface import *
from pocobus01.lab01.arquivo.arquivo import *

arq = "../data/base.txt"

if not arquivoExiste(arq):
	criarArquivo(arq)


while True:
	resposta = menu(['Passagens Compradas', 'Comprar passagem', 'Sair '])
	opc = leiaInt('Opção: ')
	if opc == 1:
		lerArquivo(arq)
	elif opc == 2:
		cont = 1
		cabecalho('Comprar passagem')
		nome = str(input('Nome: '))
		qtd = int(input(f'Quantas passagens deseja comprar, sr(a) {nome}?'))
		while cont <= qtd:
			escolha = escolhaAssentos(f'Escolha a {cont}º poltrona:')
			cont += 1
		disponiveis = obter_disponiveis()
		print(f'As passagens {escolhidos} foram reservadas, faça uma ótima viagem!')
		cadastrar(arq, nome, qtd, escolha,disponiveis)
	elif opc == 3:
		cabecalho('Sair do sistema')
	else:
		print('Informe uma opção válida')
		opc = leiaInt('Opção: ')
sleep(2)