#Desenvolvido por JhonatanDevBr[

from datetime import date

#Variáveis
atual = date.today().year
nome = str(input("Olá, como você se chama?"))
nasc = int(input("Qual foi o ano em que você nasceu?"))
idade = atual - nasc
#=========================================================

print("Os nascidos em {} tem {} anos em {}".format(nasc, idade, atual))

if  idade == 18:
    print("Você precisa se alistar este ano. Vá até a Junta de Serviço Militar mais próximo de sua residência.")
elif idade < 18:
    print("Você ainda não se encontra na idade apta para o Alistamento Militar.")
elif idade > 18:
    print("Você passou da idade necessária para o Alistamento Militar. Vá até a Junta de Serviço Militar mais próxima para se regularizar com o país.")
#=========================================================
