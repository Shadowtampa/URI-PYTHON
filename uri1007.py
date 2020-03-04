class listaPonderada:
  def __init__(self, valor):
    self.__valor = valor

  def getWealth(self):
    return self.__valor

n1 = listaPonderada(int(input()))
n2 = listaPonderada(int(input()))
n3 = listaPonderada(int(input()))
n4 = listaPonderada(int(input()))

generalWeight = n1.getWealth() * n2.getWealth() - n3.getWealth() * n4.getWealth()

print("DIFERENCA = %0.1f"%generalWeight)
