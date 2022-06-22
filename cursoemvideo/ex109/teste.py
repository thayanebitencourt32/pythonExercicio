import moeda

p =  float(input('Informe o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é  {moeda.dobro(p, True)}')
print(f'Com desconto é  {moeda.diminuir(p, 10, True)}')
