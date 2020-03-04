class vendedor:
  comissao = 0.15
  def __init__(self, nome, salarioFixo, totalVendas):
    self.__nome = nome
    self.__salarioFixo = salarioFixo 
    self.__totalVendas = totalVendas

  def getReceber(self):
    return self.__salarioFixo + (self.__totalVendas * self.comissao) 
  
  def getNome(self):
    return self.__nome

JoaozinhoPeGrande = vendedor(input(), float(input()), float(input()))

print("TOTAL = R$ %0.2f" %JoaozinhoPeGrande.getReceber())
