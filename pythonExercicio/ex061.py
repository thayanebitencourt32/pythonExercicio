print('Gerador de PA')
primeiro = int(input('Informe o termo: '))
razao = int(input('Informe a razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{}♠'.format(termo), end='')
    termo += razao
    cont += 1
