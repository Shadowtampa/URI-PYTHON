#  Orientado a Objetos por Shadowtampa
#  POO version by Shadowtampa


class Circulo:
    raio = float()


circle = Circulo()
pi = 3.14159
circle.raio = float(input())
area = pi * (circle.raio ** 2)
print('A={:.4f}'.format(area))

