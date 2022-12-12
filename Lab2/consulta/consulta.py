from Lab2.interface.interface2 import cabecalho
from tabulate import tabulate
from Lab2.listagem.listagem import listar_onibus, listar_motorista, listar_usuario, listar_cartao


def consulta_onibus():
	cabecalho('Consulta ônibus')
	dados = listar_onibus()
	print(tabulate(dados, headers='keys', tablefmt='pretty'))


def consulta_motorista():
	cabecalho('Consultar Motorista')
	dados = listar_motorista()
	print(tabulate(dados, headers='keys', tablefmt='pretty'))


def consulta_usuario():
	cabecalho('Consultar Usuário')
	dados = listar_usuario()
	print(tabulate(dados, headers='keys', tablefmt='pretty'))


def consulta_cartao():
	cabecalho('Consultar Cartão')
	dados = listar_cartao()
	print(tabulate(dados, headers='keys', tablefmt='pretty'))
