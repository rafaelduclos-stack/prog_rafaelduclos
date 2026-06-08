class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def apresentar(self):
        print(f"Nome: {self.nome} | Idade: {self.idade}")

class Aluno(Pessoa):
    def __init__(self,nome,idade,matricula):
        super().__init__(nome,idade)
        self.matricula = matricula
    def apresentar(self):
        print(f"Nome: {self.nome} | Idade: {self.idade} | Matricula: {self.matricula}")

class Professor(Pessoa):
    def __init__(self,nome,idade,salario):
        super().__init__(nome,idade)
        self.salario = salario
    def apresentar(self):
        print(f"Nome: {self.nome} | Idade: {self.idade} | Salario: {self.salario}")

pessoas = [
    Aluno("Fulano",16,1),
    Professor("Marcio",48,2300.0),
    Professor("Paulo",34,2500.0),
    Aluno("Claudia",17,2),
    Aluno("Ana",15,3)
]

for i in pessoas:
    i.apresentar()