###JOGO de DADO##

from random import randint
from operator import itemgetter
jogo = {'jogador1': randint(1,6),
         'jogador2': randint(1,6),
         'jogador3': randint(1,6),
         'jogador4': randint(1,6)}
print('Valores sorteados: ')
ranking = list()
for k, v in jogo.items():
	print(f'{k} tirou {v} no dado.')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse =True)
print(ranking)

for i,v in enumerate(ranking):
	print(f'{i+1} lugar: {v[0]} com {v[1]}')


poderia usar o sleep e importar from time import sleep