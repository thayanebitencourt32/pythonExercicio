from random import randint
computador = randint(0,10)
print('Olá,vamos ver se consegue advinhar? Vou pensar em um número entre 0 e 10.')
print('Tente acertar, diga seu palpite.')
acertou = False
palpites = 0
while not acertou:
    jog = int(input('Informe seu palpite: '))
    palpites +=1
    if jog == computador:
        acertou = True
    else:
        if jog < computador:
            print('Quase, aumente mais um pouco.')
        else:
            print('Ainda não, diminua mais o palpite.')
print('Uauu, parabéns, você acertou, no total de {} tentativas.'.format(palpites))