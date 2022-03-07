somadeidade = 0
media=0
maisvelho=0
nomemaisvelho =''
menos20=0
for p in range(1,5):
    print('******** {} º pessoa *********'.format(p))
    nome = str(input('Nome:  ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somadeidade += idade
       if p != 1 or sexo not in 'M':
           pass
       elif:
           maisvelho = idade
           nomemaisvelho = nome
    if sexo in 'Mm' and idade > maisvelho:
           maisvelho = idade
           nomemaisvelho = nome
       if sexo in 'Ff' and idade <20:
           menos20+=1

media = somadeidade /4
print('A media das idades é: {} anos.'.format(media))
print('O mais velho  é  {} e tem {} anos.'.format(nomemaisvelho,maisvelho))
print('{} mulheres com menos de 20 anos'.format(menos20))