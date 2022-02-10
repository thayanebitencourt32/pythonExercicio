salario = float(input('Qual salario atual do funcionário: '))
if salario > 1250:
    total = salario + (salario * 10/100)
    print('O novo salário, passa de R$ {:.2f}, para R$ {:.2f}.'.format(salario,total))
else:
    total = salario + (salario * 15/100)
    print('O novo salario passa de R$ {:.2f}, para R$ {:.2f}.'.format(salario,total))
