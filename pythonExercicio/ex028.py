from random import randint
from time import sleep

comp = randint(0,10) #pense nummero de 0 a 10

print('-*+*-'* 15)
print('      Vou pensar em um número de 0 a 10, consegue advinhar?')
print('-*+*-'*15)
jogador = int(input('Sua vez, em que número pensei?'))
print('checkando...')
sleep(3)
if jogador == comp:
    print('Uhu! Você acertou!')
else:
    print('Ganhei! Pensei em {} e não no {}. Tente novamente.'.format(comp,jogador))