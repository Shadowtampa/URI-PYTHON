#  Orientado a Objetos por Shadowtampa
#  POO version by Shadowtampa


class Funcionário:
    númeroFuncionário = int()
    horasTrabalhadas = int()
    valorPorHora = float()
    salário = float()


funcionário = Funcionário()

funcionário.númeroFuncionário = int(input())
funcionário.horasTrabalhadas = int(input())
funcionário.valorPorHora = float(input())

funcionário.salário = funcionário.horasTrabalhadas * funcionário.valorPorHora

print('NUMBER = {}\n'.format(funcionário.númeroFuncionário))
print('SALARY = U${:.2f}'.format(funcionário.salário))
