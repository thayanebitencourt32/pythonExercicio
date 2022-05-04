numero = list()
while True:
    n = int(input('Informe um valor: '))
    if n not in numero:
        numero.append(n)
        print('Valor adcionado com sucesso')
    else:
        print('Valor Duplicado! Não pode ser adicionado!')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
numero.sort()
print(f'Os numeros digitados na ordem crescente,são: {numero}')

