'''
Faça um programa que calcule a sequencia de Fibonacci.
Dica: Procure sobre função de recursividade.
'''
from erro import leiaInt

n = leiaInt('Quantos termos você  quer mostrar? ')
termo1 = 0
termo2 = 1
print('{} , {}'.format(termo1, termo2), end='')
contagem = 3
while contagem <= n:
    termo3 = termo1 +termo2
    print(' , {}'.format(termo3), end ='')
    termo1 = termo2
    termo2 = termo3
    contagem += 1