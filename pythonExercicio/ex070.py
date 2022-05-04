total = tot = menor= cont = 0
barato = ''

while True:
    produto = str(input('Nome do produto:  '))
    preco = float(input('Preço: RS  '))

    total += preco
    cont += 1
    if preco > 1000:
        tot += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?  [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('Lista encerrada'))
print(f'VALOR TOTAL: R$ {total}')
print(f'{tot} custaram acima de R$1000.')
print(f'O produto mais barato foi {barato} que custa R${menor}')