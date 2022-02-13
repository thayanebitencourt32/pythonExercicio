#converter inteiro para binario,octal,decimal e hexadecimal

num = int(input('Informe o número inteiro a ser convertido: '))
print('''Escolha uma das opções:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opcao = int(input('Sua opção:  '))
if opcao == 1:
    print('Convertendo {} para BINÁRIO, temos {}.'.format(num, bin(num)))
elif opcao == 2:
    print('Convertendo {} para OCTAL, temos {}.'.format(num, oct(num)))
elif opcao == 3:
    print('Convertendo {} para HEXADECIMAL, temos {}.'.format(num, hex(num)))
else:
    print('Opção inválida, tente novamente.')