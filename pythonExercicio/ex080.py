listanova = []
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > listanova[-1]: #se n for primeiro ou ultimo
        listanova.append(n)
        print('Adcionado ao final da lista')
    else:
        pos = 0
        while pos < len(listanova):
            if n <= listanova[pos]:
                listanova.insert(pos,n)
                print(f'Adcionado na posicao {pos} da lista')
                break
            pos += 1
print(f'Os valores apresentados são {listanova}')
