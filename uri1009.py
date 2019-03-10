#  Orientado a Objetos por Shadowtampa
#  POO version by Shadowtampa


class vendedor:
    nomeVendedor = str()
    vendasTotais = float()
    salário = float()


vend = vendedor()  # criação do objeto 'vendedor' com nome 'vend'

vend.nomeVendedor = str(input())
vend.salário = float(input())
vend.vendasTotais = float(input())

result = vend.salário + (vend.vendasTotais * 0.15)  # n * 0,15 <=> 15% de n

print('TOTAL = R$ {:.2f}'.format(result))
