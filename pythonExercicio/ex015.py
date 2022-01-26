km=float(input('Quantos km rodado?  '))
dias=int(input('Quantos dias ficou com carro alugado? '))
print('Como passou {} dias com o carro e rodou {} km, pagará \nR$ {:.2f}'.format(km,dias,((60*dias)+(0.15*km))))