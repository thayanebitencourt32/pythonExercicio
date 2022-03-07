from random import randint

while True:
    jogador = int(input('Diga um valor: '))
    comp = randint(0,10)
    total = jogador + comp
    tipo = ''
    while tipo not in 'PI':
        tipo =str(input('Par ou impar:  [P/I]')).strip().upper()[0]
    print('Você jogou  {} e computador jogou {}'.format(jogador,comp))
    print('Total de {}'.format(total))
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v +=1
        else:
            print('Você perdeu')
            break
    elif tipo =='I':
        if total % 2 == 1:
            print('Você venceu')
            v+=1
        else:
            print('Você perdeu')
            break
    print('Vamos tentar novamente...')
print('Game over, você venceu {}'.format(v))