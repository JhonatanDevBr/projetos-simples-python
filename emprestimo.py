#Desenvolvido por JhonatanDevBr

#Variáveis
nome = str(input("Como você se chama?"))
salario = float(input("Qual é o seu salário mensal?"))
valor_casa = float(input("Qual é o valor da casa?"))
tempo_anos = int(input("Em quantos anos você deseja quitar a sua dívida?"))
prestacao = valor_casa / (tempo_anos * 12)
minimo = salario * 30 / 100
#====================================================================================
print("Olá {}.".format(nome))
print("Para pagar uma casa de {} em {} anos".format(valor_casa, tempo_anos))
print("A prestação será de R${}".format(prestacao))
if prestacao <= minimo:
    print("Parabéns! {} Seu empréstimo foi concedido. :)".format(nome))
else:
    print("Olá, {}. Infelizmente, seu empréstimo foi negado. :(".format(nome))
#====================================================================================
