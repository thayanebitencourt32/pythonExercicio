nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

media = (nota1 + nota2)/2

if media < 5.0:
    print('VOCÊ FOI REPROVADO!')
elif media <= 6.9: # if media >=5 and media <7
    print('Você está em RECUPERAÇÃO.')
else:
    print('Parabéns, você foi APROVADO!!')