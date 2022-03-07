from datetime import date

atual = date.today().year
totmaior  = 0
totmenor = 0

for pess in range(1,8):
    nasc = int(input('Qual o ano de nascimento da {}° pessoa ?'.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('{} são menor de idade'.format(totmenor))
print('{} são maior de idade'. format(totmaior))