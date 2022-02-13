from datetime import date

atual = date.today().year  #pega o ano atual

datanascimento = int(input('Informe o ano de nascimento do atleta: '))

idade = atual - datanascimento

if idade <= 9:
    print('O atleta pertence a categoria MIRIM, tem {} anos.'.format(idade))
elif idade <= 14:
    print('O atleta pertence a categoria INFANTIL, tem {} anos.'.format(idade))
elif idade <= 19:
    print('O atleta pertence a categoria JUNIOR, tem {} anos.'.format(idade))
elif idade <=25 :
    print('O atleta pertence a categoria SÊNIOR, tem {} anos.'.format(idade))
else:
    print('O atleta é MASTER, tem {} anos.'.format(idade))