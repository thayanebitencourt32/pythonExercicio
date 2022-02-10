distancia = float(input('Informe a distância da viagem: '))
#preco=distancia *0.50 if distancia<=200 else distancia*0.45
if distancia <= 200:
    total = distancia * 0.50
    print('O valor da passagem é {:.2f}'.format(total))
else:
    print('O valor da passagem é: {:.2f}'.format(distancia*0.45))