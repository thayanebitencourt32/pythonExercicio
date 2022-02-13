print('*-*-*-*' * 5)
print(' Pedra, papel ou tesoura - JOKENPô')
print('*-*-*-*' * 5)

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador= int(input('Qual a sua jogada: '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

print('*-+-*'*5)
print('Computador apostou em {}'.format(itens[computador]))
print('Você apostou em {}'.format(itens[jogador]))
print('*-+-*'*5)

if computador == 0 :
    if jogador == 0:
       print('Empatou!')
    elif jogador == 1:
       print('Jogador venceu!')
    elif jogador == 2:
        print('Computador venceu!')
    else:
        print('Jogada inválida')
if computador == 1 :
    if jogador == 0:
       print('Computador venceu')
    elif jogador == 1:
       print('Empate!')
    elif jogador == 2:
        print('Jogador venceu!')
    else:
        print('Jogada inválida')
if computador == 2 :
    if jogador == 0:
       print('Jogador venceu!')
    elif jogador == 1:
       print('Computador venceu!')
    elif jogador == 2:
        print('Empate!')
    else:
        print('Jogada inválida')