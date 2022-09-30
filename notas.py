# Sistema de Calculadora Anual de Notas Escolares
# Desenvolvido por JhonatanDevBr
# Em desenvolvimento. Sistema ainda muito simples!

aluno = input("Digite o nome do aluno:")
b1 = int(input("Digite a nota do Primeiro Bimestre:"))
b2 = int(input("Digite a nota do Segundo Bimestre:"))
b3 = int(input("Digite a nota do Terceiro Bimestre:"))
b4 = int(input("Agora, digite a nota do Quatro Bimestre:"))

soma = b1 + b2 + b3 + b4 
media = (b1+b2+b3+b4)/4  

print("===============Informações Educacionais=================")

print("O aluno, {} possui as seguintes informações:".format(aluno))
print("Soma de todas as notas: {}".format(soma))
print("Média anual: {}".format(media))
if media<7.0:
        print("Status: Reprovado!")
elif media<10.:
        print("Status: Aprovado!")
print("===============Informações Educacionais=================")
