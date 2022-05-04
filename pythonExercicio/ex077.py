palavras = ('banana','macaco','barulho',
            'passarinho','gente', 'bonito',
            'pato','pocoyo','várias')
for p in palavras:
    print(f'\nNa palavra {p} temos: ', end=' ')
    for letra in p:
        if letra.lower() in'aeiouáàéõãíêé':
            print(letra, end=' ')