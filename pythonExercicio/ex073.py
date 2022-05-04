times = ('Corinthias', 'Palmeiras', 'Santos','Grêmio','Cruzeiro','Flamengo','Vasco','Chapecoense',
         'Atlético','Botafogo','Atlético-PR','Bahia','São Paulo','Fluminense','Sport Recife','EC Vitória',
         'Coritiba','Avaí','Ponte Preta', 'Atlético-GO')

print(f'Lista dos times do Brasileirão:  {times}')
print(f'Os cinco primeiros colocados são:  {times[0:5]}')
print(f'Os quatro ultimos colocados são: {times[-4:]}')#ele vai fazer de -4 ate os ultimos
print(f'Times na ordem alfabética: {sorted(times)}')
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição.')