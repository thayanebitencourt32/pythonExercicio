def escreva(msg):
	tam = len(msg) +4
	print('^' * tam)
	print(f'  {msg}')
	print('^' * tam)


mensagem = str(input('Informe uma mensagem: '))
escreva(mensagem)