#PALPITES PARA MEGA SENA
from random import randint
lista = list()
jogos = list()
print(' MEGA SENA ')

quant = int(input('Quer quantas surpresinhas: '))
tot = 1

while tot <= quant:
	cont = 0
	while True:
		num = randint(1, 60)
		if num not in lista:
			lista.append(num)
			cont += 1
		if cont >= 6:
			break
	lista.sort()
	jogos.append(lista[:])
	lista.clear()
	tot += 1
print('-='*3, f'Fazendo...{quant} jogos','-='*3)
for i, l in enumerate(jogos):
	print(f'Jogo {i+1}: {l}')