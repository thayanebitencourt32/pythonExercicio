qtdentrevista = mai = men = 0
pesopessoas = []
cop = []

while True:
	pesopessoas.append(str(input('Nome: ')))
	pesopessoas.append(float(input('Peso: ')))

	if len(cop) == 0:
		mai = men = pesopessoas[1]
	else:
		if pesopessoas[1] > mai:
			mai = pesopessoas[1]
		if pesopessoas[1] < men:
			men = pesopessoas[1]
	cop.append(pesopessoas[:])
	pesopessoas.clear()
	qtdentrevista += 1

	resp = str(input('Quer continuar?  [S/N]'))
	if resp in 'Nn':
		break

print(f'Os dados foram {cop}')
print(f'Foram cadastradas {qtdentrevista} pessoas.')  # ou voce cadastrou {len(pesopessoas)}
print(f'O menor peso foi {men} kg. Peso de  ', end='')
for p in pesopessoas:
	if p[1] == men:
		print(f'[{p[0]}] ', end='')
print()
print(f"O maior peso foi {mai} kg. Peso de  ", end='')
for p in pesopessoas:
	if p[1] == mai:
		print(f'[{p[0]}] ', end='')