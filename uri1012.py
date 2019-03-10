#  Orientado a Objetos por Shadowtampa
#  POO version by Shadowtampa


class Numero:
    a = float()
    b = float()
    c = float()

    def triangulo(self):
        return (self.a * self.c) / 2

    def quadrado(self):
        return self.b ** 2

    def circulo(self):
        return (self.c ** 2) * 3.14159

    def trapézio(self):
        return ((self.a + self.b) * self.c) / 2

    def retângulo(self):
        return self.a * self.b


poligono = Numero()
linha = input().split(" ")
linha = list(map(float, linha))
poligono.a, poligono.b, poligono.c = linha

print('TRIANGULO: {:.3f}'.format(poligono.triangulo()))
print('CIRCULO: {:.3f}'.format(poligono.circulo()))
print('TRAPEZIO: {:.3f}'.format(poligono.trapézio()))
print('QUADRADO: {:.3f}'.format(poligono.quadrado()))
print('RETANGULO: {:.3f}'.format(poligono.retângulo()))
