num = int(input('Informeo primeiro termo: '))
razao = int(input('Informe a razão: '))

termo = num
cont = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} => '.format(termo), end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quer mostrar mais quantos termos? '))
print('Finalizada com {} termos.'.format(termo))
