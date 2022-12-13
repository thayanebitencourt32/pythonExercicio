print('*-*-*'*10)
print('Lê um número inteiro e vê se é primo')
print('*-*-*'*10)

num = int(input('Informe um número: '))
total = 0
for c in range(1 ,  num+1):
    if num % c == 0:
        print('\033{33m', end='')
        total +=1
    else:
        print('\033[31m', end ='')
    print('{}'.format(c), end = '')
print('\n\033[m0 número {} foi divisível {} vezes'.format(num, total))
    if total != 2:
        print('O número {} não é primo.'.format(num))
    else:
        print('O número {} é primo.'.format(num))