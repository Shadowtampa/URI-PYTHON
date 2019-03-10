#  Orientado a Objetos por Shadowtampa
#  POO version by Shadowtampa


class Notas:
    valor = float()
    peso = float()


a = Notas()
b = Notas()
c = Notas()
a.peso, b.peso, c.peso = 2, 3, 5
a.valor, b.valor, c.valor = float(input()), float(input()), float(input())
result = ((a.valor * a.peso) + (b.valor * b.peso) + (c.valor * c.peso)) / (a.peso + b.peso + c.peso)  #  a * 3.5 + b * 7.5  /  11 <=> 3.5+7.5

print('MEDIA = {:.1f}'.format(result))


