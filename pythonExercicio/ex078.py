listanova = []
main = 0
men = 0
for c in range(0 , 5):
    listanova.append(int(input(f'Informe um numero para a posição {c}:  ')))
    if c==0:
        mai = men = listanova[c]
    else:
        if listanova[c] > mai:
            mai = listanova[c]
        if listanova[c] < men:
            men = listanova[c]
print(f'Você digitou os valores{listanova} ')
print(f'O maior valor digitado foi {mai} nas posições ',end='')
for i,v in enumerate(listanova):
    if v == mai:
        print(f'{i}..',end='')
print()
print(f'O menor valor digitado foi {men} nas posições ',end='')
for i,v in enumerate(listanova):
    if v == men:
        print(f'{i}..', end='')
print()