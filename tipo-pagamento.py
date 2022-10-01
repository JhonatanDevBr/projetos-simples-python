#Desenvolvido por JhonatanDevBr


preco = float(input("Qual é o valor total da compra?"))
print("{:=^40}".format(" MERCADINHO BOM PREÇO "))
print(''' Escolha a Forma de Pagamento:

[1]: à vista c/ '10%' de desconto
[2]: 2x no cartão s/ juros
[3]: 3x no cartão s/ juros
[4]: 4x ou mais no cartão c/ juros''')
print("{:=^40}".format("=========================="))
opcao = int(input('Selecione a opção desejada:'))
if opcao == 1:
    total = (preco * 10 / 100)
    print("A compra no valor de R$ {} ficará no total de: R$ {}.".format(preco, total))
elif opcao == 2:
    total = (preco / 2)
    print("A compra no valor de R$ {} ficará em duas parcelas de R$ {} s/juros.".format(preco, total))
elif opcao == 3:
    total = (preco / 3)
    print("A compra no valor de R$ {} ficará em três parcelas de R$ {} s/juros.".format(preco, total))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    parcelas = int(input("Quantas parcelas? (Máximo 12x c/ juros)."))
    total_parcelado = total / parcelas
    print("Sua compra de R$ {} será parcelada em {} vezes de R$ {} c/ '20%' de juros.".format(preco, parcelas, total_parcelado))
else:
    print("Opção invalida.")