import moeda

p =  float(input('Informe o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é  {moeda.moeda(moeda.dobro(p))}')
print(f'O desconto de {taxa}% é  {moeda.moeda(moeda.diminuir(p, 10))}')
