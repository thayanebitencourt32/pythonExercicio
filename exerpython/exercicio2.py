"""
Essa função irá ler 4 números, calcular as expressões: soma dos 2 últimos e multiplicação dos dois primeiros.
Se a multiplicação dos 2 primeiros for impar exibir “a”.
Se a soma dos dois últimos for par exibir “b”.
"""
from exerpython.erro import leiaInt

numeros = []
i = 1


def number():
	for i in range(1,5):
		numero = leiaInt(f'Informe o número {i}:  ')
		numeros.append(numero)
	soma = numeros[2] + numeros[3]
	mult = numeros[0] * numeros[1]
	if soma % 2 == 0:
		print('b')
	if mult % 2 != 0:
		print('a')

number()
