print('*-*-*-*' * 3) #{:=^40}
print('Simulador de loja')
print('*-*-*-*-*'* 3)

preco = float(input('Informe o valor das compras: R$ '))

print('''SELECIONE A OPÇÃO DE PAGAMENTO:
[1] Á VISTA (DINHEIRO/CHEQUE)
[2] Á VISTA (CARTÃO)
[3] CARTÃO DE CRÉDITO (ATÉ 2X)
[4] CARTÃO DE CRÉDITO (3X OU MAIS) ''')
opcao = int(input('Qual é a opção de pagamento:  '))

if opcao == 1:
    total = preco - (preco * 10/100)
elif opcao == 2:
    total = preco - (preco * 5/100)
elif opcao == 3:
    total = preco / 2
elif opcao == 4:
    total = preco + (preco *20/100)
    totalparc = int (input ('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {} x de R${:.2f} no final'.format(totalparc , total))
else:
    total = 0
    print('Opção inválida.')
print('Sua compra de R${} , vai para:  R${:.2f}'.format(preco, total))
