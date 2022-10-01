#Desenvolvido por JhonatanDevBr

import random 
#------------------------Variáveis---------------------------------
alfabeto_minusculo = 'abcdefghijklmnopqrstuvwxyz'
alfabeto_maisculo = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
simbolos = '[]{}()*#;/,-_%'
numeros = '0123456789'
simbolos = '[]{}()*#;/,-_%'
nome = str((input('Olá. Bem-vindo. Digite o seu nome para começarmos:')))
quantidade = int(input('Agora, {}, digite o tamanho da senha que você está precisando. (Min 10; Max 30)'.format(nome)))
tamanho = quantidade
gerador = simbolos + alfabeto_maisculo + alfabeto_minusculo + numeros
senhagerada = "".join(random.sample(gerador,tamanho))
#------------------------Funções---------------------------------
if quantidade >= 10 and quantidade <= 30:
    print("{:=^40}".format("=======Gerador de Senhas======="))
    print('Sua senha foi gerada com Sucesso!')
    print("Solicitante: {}".format(nome))
    print("Tamanho de Senha Digitado: {}".format(quantidade))
    print("Aqui está a sua senha gerada: {:^10}".format(senhagerada))
    print("{:=^40}".format("=======Gerador de Senhas======="))
else:
    print("{:=^40}".format("=======Gerador de Senhas======="))
    print('Sua senha não foi gerada!')
    print("Solicitante: {}".format(nome))
    print("Motivo: Tamanho da senha não condiz com o permitido.")
    print("Quantidade escolhida: {}".format(tamanho))
    print("{:=^40}".format("=======Gerador de Senhas======="))

#-------------------------------------------------------------------