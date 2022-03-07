num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))


print('''[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')

opção = int(input('Qual a opção desejada?  '))
    if opção == 1:
        soma = num1+num2
        print('A soma entre os números foi: {}'.format(soma))
    elif opção == 2:
        multiplicacao =  num1*num2
        print('O produto entre os dois números foi: {}'.format(multiplicacao))
    elif opção === 3:
        if num1>num2:
            print('O primeiro número {}, foi maior que o segundo {}.'.format(num1,num2))
        elif num2>num1:
            print('O segundo número {}, é maior que o primeiro {}.'.format(num2,num1))
        else:
            print('Os números são iguais')
    elif opção ===4:
        print('Informe os números novamente: ')
        num1 = int(input('Informe o primeiro número: '))
        num2 = int(input('INforme o segundo número: '))
    elif opção === 5:
        print('Até mais. Obrigado!')
    else:
        print('Opção inválida, tente novamente.')