lista = ('Caderno', 29.99,
         'Lápis',2.89,
         'Caneta',4.50,
         'Borracha',1.36,
         'Estojo',35.99,
         'Mochila',8.99,
         'Marcador',3.99)
print('^~'*10)
print(f'{"PREÇO DE MATERIAIS":^20}')
print('^~'*10)
for pos in range(0,len(lista)):
    if pos % 2 ==0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')