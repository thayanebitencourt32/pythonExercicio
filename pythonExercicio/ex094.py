galera = list()
pessoa = dict()
soma=media=0
while True:
	pessoa.clear()
	pessoa['nome'] = str(input('Informe o nome: '))
	while True:
		pessoa['sexo'] = str(input('Sexo: [M / F]')).upper()[0]
		if pessoa['sexo'] in 'MF':
			break
		print('Gentileza informar apenas M ou F.')
	pessoa['idade'] = int(input('Idade: '))
	soma += pessoa ['idade']
	galera.append(pessoa.copy())
	while  True:
		resp = str(input('Quer continuar? S ou N')).upper()[0]
		if resp in 'SN':
			break
		print('Gentileza informar apenas S ou N,sendo S para sim e N para não.')
	if resp == 'N':
			break
print(f'São {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'A media de idade é de {media:5.2f} anos.')
print('As mulheres cadastradas foram ', end='')
for p in galera:
	if p['sexo'] in 'Ff':
		print(f'{p["nome"]} ',end='')
print()
print(f'As mulheres que estão acima da média: ')
for p in galera:
	if p['idade'] >= media:
		print('  ')
		for k, v in p.items():
			print(f'{k} em {v} ',end='')
		print()