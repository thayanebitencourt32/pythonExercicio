teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:]) #se não colocar o :ele vai fazer maria 22,duas vezes
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

gal = list()
dado = list()
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()