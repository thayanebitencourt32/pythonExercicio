import datetime
from random import randint
from Lab2.banco import cursor
from Lab2.interface.interface2 import checarEmail, leiaInt, leiaString


escolha = 0

def incluirUsuario(cabecalho):
	cabecalho('Cadastrar novo usuário')
	nome = leiaString('Informe o nome: ')
	sobrenome = leiaString('Informe o sobrenome: ')
	email = checarEmail()
	bairro = leiaString('Bairro:')
	datanasc = input('Data de nascimento:  dd/mm/yyyy ')
	datanasc= datanasc.split('/')
	datanasc= datetime.datetime(int(datanasc[2]), int(datanasc[1]), int(datanasc[0]))
	numcartao = randint(0000000, 9999999)
	print(f'Usuário cadastrado com sucesso, cartao {numcartao}')
	return nome, sobrenome, email, bairro, datanasc, numcartao


def set_usuario(nome, sobrenome, email, bairro, datanasc, numcartao):
	nome = nome
	sobrenome = sobrenome
	email = email
	bairro = bairro
	datanasc = datanasc
	numcartao = numcartao
	vsql = f"""INSERT INTO thayane_bitencourt.usuario (nome, sobrenome, email, bairro, datanasc, numcart) VALUES ('{nome}','{sobrenome}','{email}','{bairro}','{datanasc}',{numcartao})"""
	cursor.execute(vsql)
	cursor.commit()


def incluirMotorista(cabecalho):
	cabecalho('Cadastrar novo motorista')
	cnh = leiaInt('Informe a CNH do motorista: ')
	nomedomoto = leiaString('Informe o nome do motorista: ')
	sobrenomedomoto = leiaString('Informe o sobrenome do motorista: ')
	datanascmoto = input('Data de nascimento:  dd/mm/yyyy ')
	datanascmoto= datanascmoto.split('/')
	datanascmoto=datetime.datetime(int(datanascmoto[2]), int(datanascmoto[1]), int(datanascmoto[0]))
	idmotor = randint(000000, 999999)
	print(f'Motorista cadastrado com sucesso, id:{idmotor}')
	return cnh, nomedomoto, sobrenomedomoto, datanascmoto, idmotor


def set_motorista(cnh, nomedomoto, sobrenomedomoto, datanascmoto, idmotor):
	cnh = cnh
	nomedomoto = nomedomoto
	sobrenomedomoto = sobrenomedomoto
	datanascmoto = datanascmoto
	idmotor = idmotor
	vsql = f"""INSERT INTO thayane_bitencourt.motorista (cnh,nomedomoto,sobrenomedomoto,datanascmoto,idmotor) VALUES ({cnh},'{nomedomoto}','{sobrenomedomoto}','{datanascmoto}',{idmotor}) """
	cursor.execute(vsql)
	cursor.commit()


def incluirCartao(cabecalho,menu):
	cabecalho('Cadastrar novo cartão')
	numcartao = randint(0000000, 9999999)
	print('Escolha o tipo de cartão:')
	menu(['Comum', 'estudante', 'vale-transporte', 'idoso'])
	tipocartao = leiaInt('Opção: ')
	credito = leiaInt('Informe o valor que irá inserir de credito: ')
	emissao = datetime.datetime.now()
	print(f'Cartão de {tipocartao} cadastrado com sucesso, Número:{numcartao}, emitido em : {emissao}, com crédito de R$ {credito}')
	return numcartao, tipocartao, credito, emissao


def set_cartao(numcartao, tipocartao, credito, emissao):
	numcartao = numcartao
	tipocartao = tipocartao
	credito = credito
	emissao = emissao
	vsql = f"""INSERT INTO [thayane_bitencourt].[cartao] (numcartao,tipocartao, credito,emissao) VALUES ({numcartao},'{tipocartao}',{credito},'{emissao}') """
	cursor.execute(vsql)
	cursor.commit()


def incluirOnibus(cabecalho, menu):
	cabecalho('Cadastrar novo ônibus')
	menu(['Urbana', 'Rural'])
	print('Escolha o tipo de linha.')
	linha = leiaInt('Opção: ')
	placa = leiaInt('Informe a placa: ')
	menu(['Mercedes','Volkswagem','Marcopolo','Scania','Agrale','Outro'])
	print('Escolha o modelo do ônibus.')
	modelo = leiaInt('Informe o modelo do ônibus: ')
	ano = leiaInt('Ano de fabricação: ')
	idmotor = leiaInt('Informe cnh do motorista: ')
	print(f'Ônibus placa {placa}  cadastrado com sucesso, para motorista de cnh {idmotor}!')
	return linha, placa, modelo, ano, idmotor


def set_onibus(linha, placa, modelo, ano, idmotor):
	linha = linha
	placa = placa
	modelo = modelo
	ano = ano
	idmotor = idmotor
	vsql = f"""INSERT INTO [thayane_bitencourt].[onibus] (linha, placa,modelo, ano, idmotor) VALUES ({linha},{placa},'{modelo}','{ano}',{idmotor})"""
	cursor.execute(vsql)
	cursor.commit()
