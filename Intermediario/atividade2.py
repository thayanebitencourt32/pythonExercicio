'''
 Faça uma função que retorna a quantidade de vogais em uma frase.
'''
from erro import leiaString


def contaVogais():
	cont = 0
	frase = leiaString('Informe a frase, para contagem de vogais: ').strip().lower()
	for vogal in frase:
		if vogal in 'aeiouáàéõãíêé':
			cont += 1
	print(f'A quantidade de vogais na frase é: {cont}')


contaVogais()