valorcasa = float(input('Qual o valor do imóvel desejado? R$ '))
salcomprador = float(input('Informe seu salário:R$  '))
anos = int(input('Pretende pagar em quantos anos? '))

prestacao = valorcasa/(anos * 12)
minimo =  salcomprador * 30 / 100
if prestacao <= minimo:
    print('O empréstimo poderá ser CONCEDIDO. Valor da prestação: R${:.2f}'.format(prestacao))
else:
    print('Empréstimo NEGADO, valor da prestação excede 30% do salário.')