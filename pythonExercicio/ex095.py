
time = list()
dados = dict()
partida = list()

while True:
	dados.clear()
	dados['nome'] = str(input('Informe o nome do jogador: '))
	tot = int(input(f'Informe o número de partidas jogadas por {dados["nome"]}: '))
	partida.clear()
	for c in range(0, tot):
		partida.append(int(input(f'Quantos gols na {c}° partida? ')))
	dados['gols'] = partida[:]
	dados['total'] = sum(partida)
	time.append(dados.copy())
	while True:
		resp = str(input('Quer continuar S/M')).upper()[0]
		if resp in 'SN':
			break
		print('Gentileza informar apenas S ou N')
	if resp == 'M':
		break
print('cod ', end ='')
for i in dados.keys():
	print(f'{i:>15}', end='')
print()

for k, v in enumerate(time):
	print(f'{k:>3}', end='')
	for d in v.values():
		print(f'{str(d):<15}', end='')
	print()
while True:
	busca = int(input('Mostrar dados de que jogador: (333 para sair'))
	if busca == 333:
		break
	if busca >= len(time):
		print(f'Não tem jogador com esse codigo {busca}')
	else:
		print(f'Dados do jogador {time[busca] ["nome"]} :')
		for i, g in enumerate(time[busca]['gols']):
			print(f' No jogo {i+1} fez {g} gols.')