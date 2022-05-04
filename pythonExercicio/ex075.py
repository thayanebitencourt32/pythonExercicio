numeros = (int(input('Informe um número: ')), int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')), int(input('Informe o último número: ')))

print(f'Os números foram: {numeros}')
print(f'O número 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O valor 3 apareceu {numeros.index(3)+1}ª na posição')
else:
    print('O valor 3 não apareceu em nenhuma posição')


print('Os valores pares digitados foram: ', )

for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
