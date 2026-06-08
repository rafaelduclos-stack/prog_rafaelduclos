class Funcionario:
    def __init__(self,nome,matricula,salario):
        self.__nome = nome #n pd ser vazio
        self.__matricula = matricula #n pd ser negativa
        self.__salario = salario #n pd ser negativo

    def set_nome(self,nome): #nome
        if len(nome) > 0:
            self.__nome = nome
        else:
            print("Erro: campo de nome não pode estar vazio")
        
    def get_nome(self):
        return self.__nome

    def set_matricula(self,matricula): #matricula
        if 1 <= matricula:
            self.__matricula = matricula
        else:
            print("Erro: matrícula deve ser positiva, diferente de 0") 

    def get_matricula(self):
        return self.__matricula

    def set_salario(self,salario): #salario
        if 0 <= salario:
            self.__salario = salario
        else:
            print("Erro: salário não deve ser negativo.")

    def get_salario(self):
        return self.__salario
        
    def calcular_salario(self): #metodo polimorfico
        return self.__salario
    
    def exibir(self):
        print(f"Nome: {self.__nome} | Matricula: {self.__matricula} | Tipo: {type(self).__name__} | Salario: {self.calcular_salario()}")

class CLT(Funcionario):
    def __init__(self, nome, matricula, salario):
        super().__init__(nome,matricula,salario)

class Vendedor(Funcionario):
    def __init__(self,nome,matricula,salario,vendas):
        super().__init__(nome,matricula,salario)
        self.__vendas = vendas
    
    def get_vendas(self):
        return self.__vendas

    def set_vendas(self,vendas):
        if 0 <= vendas:
            self.__vendas = vendas
        else:
            print("Erro: vendas não podem ser negativas")
    
    def calcular_salario(self):
        return self.get_salario() + (self.__vendas/10)

class Gerente(Funcionario):
    def __init__(self,nome,matricula,salario):
        super().__init__(nome,matricula,salario)

    def calcular_salario(self):
        return self.get_salario() + 1500.0

funcionarios = [
    CLT("Rafael",1,2500.0),
    Vendedor("Lucas",2,3000.0,10000.0),
    Gerente("Julia",3,5000.0),
    CLT("Jonas",4,2600.0),
    Vendedor("Ana",5,3500.0,12000.0),
    Vendedor("Matheus",6,2900.0,9000.0)
]

for i in funcionarios:
    i.exibir()