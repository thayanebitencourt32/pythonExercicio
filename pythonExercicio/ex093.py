
dados = dict()
partida = list()

dados['nome'] = str(input('Informe o nome do jogador: '))
tot = int(input(f'Informe o número de partidas jogadas por {dados["nome"]}: '))
for c in range(0, tot):
	partida.append(int(input(f'Quantos gols na {c}° partida? ')))
dados['gols'] = partida[:]
dados['total'] = sum(partida)
print(dados)

for k, v in dados.items():
	print(f' O campo {k} tem o valor {v}')
print(f'O jogador {dados["nome"]} jogou {len(dados["gols"])} partidas.')
for i, v in enumerate(dados['gols']):
	print(f' => Na partida {i}, fez {v} gols.')
print(f'Contabilizando {dados["total"]} gols')