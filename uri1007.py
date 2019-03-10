#  Orientado a Objetos por Shadowtampa
#  POO version by Shadowtampa


class Numero:
    valor = int()


a = Numero()
b = Numero()
c = Numero()
d = Numero()

a.valor, b.valor, c.valor, d.valor = int(input()), int(input()), int(input()), int(input())

result = a.valor * b.valor - c.valor * d.valor  # A * B - C * D

print('DIFERENCA = {}'.format(result))


