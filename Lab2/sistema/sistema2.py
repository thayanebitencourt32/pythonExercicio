from Lab2.cadastro.cadastro import incluirUsuario, set_usuario, incluirMotorista, set_motorista, incluirCartao, set_cartao, incluirOnibus, set_onibus
from Lab2.consulta.consulta import consulta_usuario, consulta_cartao, consulta_onibus, consulta_motorista
from Lab2.interface.interface2 import *


while True:
	resposta = menu(['Cadastrar usuário', 'Cadastrar Cartão', 'Cadastrar ônibus', 'Cadastrar motorista', 'Realizar consulta','Sair '])
	opc = leiaInt('Opção: ')
	if opc == 1:
		nome, sobrenome, email, bairro, datanasc, numcartao = incluirUsuario(cabecalho)
		set_usuario(nome=nome, sobrenome=sobrenome, email=email, bairro=bairro, datanasc=datanasc, numcartao=numcartao)
	elif opc == 2:
		numcartao, tipocartao, credito, emissao = incluirCartao(cabecalho, menu)
		set_cartao(numcartao=numcartao, tipocartao=tipocartao, credito=credito, emissao=emissao)
	elif opc == 3:
		linha, placa, modelo, ano, idmotor = incluirOnibus(cabecalho, menu)
		set_onibus(linha=linha, placa=placa, modelo=modelo, ano=ano, idmotor=idmotor)
	elif opc == 4:
		cnh, nomedomoto, sobrenomedomoto, datanascmoto, idmotor = incluirMotorista(cabecalho)
		set_motorista(cnh=cnh, nomedomoto=nomedomoto, sobrenomedomoto=sobrenomedomoto, datanascmoto=datanascmoto, idmotor=idmotor)
	elif opc == 5:
		cabecalho('Informe o que deseja consultar: ')
		resposta = menu(['Consulta usuário', 'Consultar Cartão', 'Consultar ônibus', 'Consultar motorista', 'Sair'])
		opc = leiaInt('Opção: ')
		if opc == 1:
			consulta_usuario()
		elif opc == 2:
			consulta_cartao()
		elif opc == 3:
			consulta_onibus()
		elif opc == 4:
			consulta_motorista()
		else:
			print('Informe uma opção válida')
		opc = leiaInt('Opção: ')
sleep(2)
