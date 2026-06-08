class Funcionario:
    def __init__(self,salario):
        self.salario = salario  
    def calcular_salario(self):
        return 0

class Vendedor(Funcionario):
    def __init__(self,salario,comissao):
        super().__init__(salario)
        self.comissao = comissao
    def calcular_salario(self):
        return self.salario + (self.comissao/10)

class Gerente(Funcionario):
    def __init__(self,salario,bonus):
        super().__init__(salario)
        self.bonus = bonus
    def calcular_salario(self):
        return self.salario + self.bonus

vendedor = Vendedor(4000.0,13000.0)
gerente = Gerente(7000.0,500.0)
print(vendedor.calcular_salario())
print(gerente.calcular_salario())