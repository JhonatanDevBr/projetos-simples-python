# Desenvolvido por JhonatanDevBr

dias = int(input("Por quantos dias o veículo será alugado?"))
km = float(input("Quantos quilômetros?"))
vec = input("Qual o veículo?")
mod = input("Qual o modelo do veículo?")

total = (dias * 45 ) + (km * 0.80)

print("================Aluguel====================")
print("Veículo: ({})".format(vec))
print("Modelo: ({})".format(mod))
print("Quilômetros Rodados: {} Km".format(km))
print("Dias de aluguel: {} dias".format(dias))
print("Subtotal: R${}".format(total))
print("================Aluguel====================")

