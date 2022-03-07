while True:
    n = int(input('Qual numero deseja ver tabuada:  '))
    if n < 0:
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c} ')