# ORIENTADO A OBJETOS por Shadowtampa
class peca:
  def __init__(self, linhaEntrada):
    self.__linhaEntrada = linhaEntrada.split(" ")
    self.__codigo, self.__nmrPc, self.__vlrUnit = self.__linhaEntrada
  def getCustoTotal(self):
    return float(self.__nmrPc) * float(self.__vlrUnit)

pc1 = peca(input())
pc2 = peca(input())

custoTotal = pc1.getCustoTotal() + pc2.getCustoTotal()

print("VALOR A PAGAR: R$ %0.2f"%custoTotal)

#########################################################################################################################################


linha1 = input().split(" ")
linha2 = input().split(" ")

cod1, qtde1, valor1 = linha1
cod2, qtde2, valor2 = linha2

total = (int(qtde1) * float(valor1)) + (int(qtde2) * float(valor2))

print("VALOR A PAGAR: R$ %0.2f" %total)

