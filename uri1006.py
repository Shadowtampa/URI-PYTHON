class listaPonderada:
  def __init__(self, valor, peso):
    self.__valor = valor
    self.__peso = peso 

  def getWeight(self):
    return self.__peso 

  def getWealth(self):
    return self.__valor * self.__peso

n1 = listaPonderada(float(input()),2)
n2 = listaPonderada(float(input()),3)
n3 = listaPonderada(float(input()),5)

generalWeight = n1.getWeight() + n2.getWeight() + n3.getWeight()
generalWealth = n1.getWealth() + n2.getWealth() + n3.getWealth()

avg = generalWealth / generalWeight

print("MEDIA = %0.1f"%avg)
