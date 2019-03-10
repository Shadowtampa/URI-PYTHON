#  Orientado a Objetos por Shadowtampa

class Esfera:
    raio = float()


esfera = Esfera()
esfera.raio = float(input())  # volume = (4/3) * pi * R3
volume = (4/3) * 3.14159 * (esfera.raio ** 3)
print('VOLUME = {:.3f}'.format(volume))
