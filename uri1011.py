class esfera:
  def __init__(self, raio):
    self.__raio = raio
    self.__pi = 3.14159
    self.__k = 4.0/3
  def getVolume(self):
    return self.__k * self.__pi * (self.__raio ** 3)

bolitakkkk = esfera(float(input()))

print("VOLUME = %0.3f" %bolitakkkk.getVolume())
