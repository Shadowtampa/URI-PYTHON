#  Orientado a Objetos por Shadowtampa
#  POO version by Shadowtampa


class Carro:
    def __init__(self, distância, combustível):
        self.distância = distância
        self.combustível  = combustível

    def Consumo(self):
        return self.distância / self.combustível


a, b = float(input()), float(input())
carro = Carro(a, b)
print('{:.3f} km/l'.format(carro.Consumo()))
