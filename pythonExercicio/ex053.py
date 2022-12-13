from typing import List

print('Testar se é palíndromo')

frase = str(input('Digite a frase')).strip().upper()
palavras= frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
    if junto == inverso:
        print('A frase é palímetro.')
    else:
        print('A frase não é palímetro.')

