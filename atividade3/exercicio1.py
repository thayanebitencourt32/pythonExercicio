"""
Ler três valores para os lados de um triângulo, considerando lados como: A, B e C.
Verificar se os lados fornecidos formam realmente um triângulo, e se esta condição for verdadeira,
informar se o triângulo é isósceles, escaleno ou equilátero.
"""
from erro import leiaFloat

def tipoTriangulo():
	a = leiaFloat('Informe o primeiro segmento: ')
	b = leiaFloat('Informe o segundo segmento: ')
	c = leiaFloat('Informe o terceiro segmento: ')

	if a < b + c and b < a + c and c < a + b:
		print('Os segmentos podem formar  um TRIÂNGULO: ')
		if a == b and b == c:
			print('EQUILÁTERO.')
		elif a != b != c != a:
			print('ESCALENO.')
		else:
			print('ISÓSCELES.')
	else:
		print('Os segmentos não podem formar TRIÂNGULO.')



tipoTriangulo()