class Funcionario:
    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario
    def exibir(self):
        print(f"Nome: {self.nome} | Salario: {self.salario}")

class Gerente(Funcionario):
    def __init__(self,nome,salario,bonus):
        super().__init__(nome,salario)
        self.bonus = bonus
    def salario_total(self):
        return self.salario + self.bonus
    def exibir(self):
        print(f"Nome: {self.nome} | Salario: {self.salario_total()}")

gerente = Gerente("Rafael",5000.0,1500.0)
gerente.exibir()