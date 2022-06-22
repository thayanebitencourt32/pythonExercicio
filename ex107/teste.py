import moeda

p =  float(input('Informe o preço: R$ '))
print(f'A metade de {p} é R$ {moeda.metade(p)}')
print(f'O dobro de {p} é R$ {moeda.dobro(p)}')
print(f'O desconto de {p} é R$ {moeda.diminuir(p)}')
