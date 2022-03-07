from math import factorial
num= int(input('Informe um número para calcular fatorial: '))
f = factorial(num)
print('O fatorial de {} é {}.'.format(num,f))


n = int(input('Informe um numero: '))
c = n
f = 1
while c > 0:
    print('{}'.format(c), end='')
    print('x'if c > 1 else '=', end='')
    f *= c
    c -= 1
print('O fatorial de {} é {}.'.format(n, f))