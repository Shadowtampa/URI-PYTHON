# ORIENTADO A OBJETOS por Shadowtampa
class Produto:
    ID = int(1)
    quantidade = float()
    valor = float()


prod1 = Produto()
prod2 = Produto()
linha1 = input().split(" ")
linha2 = input().split(" ")

prod1.ID, prod1.quantidade, prod1.valor = linha1
prod2.ID, prod2.quantidade, prod2.valor = linha2
total = (float(prod1.quantidade)) * (float(prod1.valor)) + (float(prod2.quantidade)) * (float(prod2.valor))


print('VALOR A PAGAR: R$ {:.2f}'.format(total)

#########################################################################################################################################


linha1 = input().split(" ")
linha2 = input().split(" ")

cod1, qtde1, valor1 = linha1
cod2, qtde2, valor2 = linha2

total = (int(qtde1) * float(valor1)) + (int(qtde2) * float(valor2))

print("VALOR A PAGAR: R$ %0.2f" %total)

