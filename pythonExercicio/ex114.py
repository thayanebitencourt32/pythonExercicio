import urllib
import urllib.request


try:
	site = urllib.request.urlopen('https://docs.microsoft.com/pt-br/learn/paths/azure-data-fundamentals-explore-non-relational-data/')
except urllib.error.URLError:
	print('O site não esta acessivel no momento')
else:
	print('O acesso foi feito com sucesso')
	print(site.read())
