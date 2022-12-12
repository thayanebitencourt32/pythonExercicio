"""
Programa que vai ler dois números, multiplicar e apresentar resultado,
caso seja maior que 15.
"""
from exerpython.erro import leiaInt


n1 = leiaInt('Informe um número inteiro: ')
n2 = leiaInt('Informe outro número inteiro: ')
resultado = n1 * n2
if resultado > 15:
	print(f'O resultado foi maior que 15. A multiplicação dos números foi {resultado}')
else:
	print('Obrigado!')