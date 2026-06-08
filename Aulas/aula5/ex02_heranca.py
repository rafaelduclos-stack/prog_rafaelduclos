class Veiculo:
    def __init__(self,marca,ano):
        self.marca = marca
        self.ano = ano
    def informacoes(self):
        print(f"Marca: {self.marca} | Ano: {self.ano}")

class Carro(Veiculo):
    def __init__(self,marca,ano,portas):
        super().__init__(marca,ano)
        self.portas = portas
    def informacoes(self):
        print(f"Marca: {self.marca} | Ano: {self.ano} | Portas: {self.portas}")

class Moto(Veiculo):
    def __init__(self,marca,ano,cilindradas):
        super().__init__(marca,ano)
        self.cilindradas = cilindradas
    def informacoes(self):
        print(f"Marca: {self.marca} | Ano: {self.ano} | Cilindradas: {self.cilindradas}")

c1 = Carro("Renault","Logan",4)
m1 = Moto("Honda","CG 160",1000)
c1.informacoes()
m1.informacoes()