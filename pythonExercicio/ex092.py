from datetime import datetime

dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year-nasc
dados['ctps'] = int(input('Carteira de trabalho ( 0 caso não tenha)'))
if dados['ctps'] != 0:
	dados['contratacao']= int(input('Informe o ano de contratação: '))
	dados['salario'] = float(input('Informe o salário: '))
	dados['aposentadoria'] = dados['idade']+((dados['contratacao'] + 35) - datetime.now().year)

for k, v in dados.items():
	print(f'{k} tem o valor {v}')
