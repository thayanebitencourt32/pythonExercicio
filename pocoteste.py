
from colorama import init, Fore, Back, Style

init(autoreset=True)  # set the autoreset to True so we don't have to reset it manually
# 1 == motorista
# 0 == assento inexistente / corredor
# 2 == assento disponível
# 3 == assento vendido
# Criando uma matriz que designa o onibus
onibus = [[1, 0, 0, 0, 0]]
onibus.append([2, 2, 0, 2, 2])
onibus.append([2, 3, 0, 2, 2])

#onibus[0][0] -> 1 motorista
# Printando o onibus e colorindo ele
for linha in range(3):
    for coluna in range(5):
        if onibus[linha][coluna] == 1:  # é o motorista
            print(f'{Back.WHITE}{Fore.BLACK} {linha}{coluna} ', end=' ')
        elif onibus[linha][coluna] == 0:  # é um corredor
            print(f'{Back.BLUE}{Fore.BLACK} {linha}{coluna} ', end=' ')
        elif onibus[linha][coluna] == 2:  # assento disponível
            print(f'{Back.GREEN}{Fore.BLACK} {linha}{coluna} ', end=' ')
        elif onibus[linha][coluna] == 3:  # assento vendido
            print(f'{Back.RED}{Fore.BLACK} {linha}{coluna} ', end=' ')

    if coluna == 4:
        print('')


		if linha == 0 or coluna == 2:
			if numero == 5:
				numeros.append('MT')
			else:
				numeros.append('C')