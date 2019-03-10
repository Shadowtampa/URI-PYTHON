#  Orientado a Objetos por Shadowtampa
#  POO version by Shadowtampa


class Numero:
    valor = int()


a = Numero()
b = Numero()
a.valor, b.valor = int(input()), int(input())
result = a.valor * b.valor

print('PROD = {}'.format(result))


