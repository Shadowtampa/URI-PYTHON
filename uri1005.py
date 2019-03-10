#  Orientado a Objetos por Shadowtampa
#  POO version by Shadowtampa


class Numero:
    valor = float()
    peso = float()


a = Numero()
b = Numero()
a.peso, b.peso = 3.5, 7.5
a.valor, b.valor = float(input()), float(input())
result = ((a.valor * a.peso) + (b.valor * b.peso)) / (a.peso + b.peso)  # a * 3.5 + b * 7.5  /  11 <=> 3.5+7.5

print('MEDIA = {:.5f}'.format(result))


