from random import shuffle

n1  = str(input('Informe nome do primeiro aluno: '))
n2 =  str(input('Informe nome do segundo aluno: '))
n3 =  str(input('Informe nome do terceiro aluno: '))
n4 = str(input('Informe nome do quarto aluno: '))

lista = [n1,n2,n3,n4]

shuffle(lista)
print('A ordem a apresentar, será: ')
print(lista)
