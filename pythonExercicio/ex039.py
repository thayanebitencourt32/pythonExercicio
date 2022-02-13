from datetime import date

atual = date.today().year

print('''Informe:
[1] FEMININO
[2] MASCULINO''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('Você não precisa se alistar. No Brasil, apenas sexo masculino.')
elif opcao == 2:
  anonasc = int(input('Informe seu ano de nascimento: '))
  idade = atual - anonasc

  print('Em {} você tem {} anos.'.format(atual, idade))

  if idade < 18:
      saldo = 18 - idade
      ano = atual + saldo
      print('Ainda vai se alistar ao serviço militar. Faltam {} anos para se alistar, você vai se alistar em {}'.format(
          saldo, ano))
  elif idade == 18:
      print('HORA DE SE ALISTAR!')
  else:
      saldo = idade - 18
      ano = atual - saldo
      print('Infelizmente passou do prazo de alistamento. Deveria ter se alistado há {} anos, em {}'.format(saldo, ano))

else:
    print('Opção invalida')


