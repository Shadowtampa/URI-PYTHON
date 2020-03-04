class funcionario:
  def __init__(self, numero, horas, valorRecebido):
    self.__numero = numero
    self.__horas = horas
    self.__valorRecebido = valorRecebido

  def getWage(self):
    return self.__horas * self.__valorRecebido
  
  def getNumber(self):
    return self.__numero

JoaozinhoPeGrande = funcionario(int(input()), int(input()), float(input()))

salario = JoaozinhoPeGrande.getWage()

print("NUMBER =",JoaozinhoPeGrande.getNumber(), "\nSALARY = U$ %0.1f"%salario)
