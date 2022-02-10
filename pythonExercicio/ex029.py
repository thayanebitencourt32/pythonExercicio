vel = float(input('Qual a velocidade do carro?  '))

if vel > 80:
    valor= vel - 80
    print('MULTADO! Você excedeu o limite, pagará R${:.2f} de multa. '.format(valor*7))

print('Tenha um bom dia e dirija com segurança!')
