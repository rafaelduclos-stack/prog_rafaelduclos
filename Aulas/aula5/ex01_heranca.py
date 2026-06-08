class Animal:
    def __init__(self,nome):
        self.nome = nome
    def comer(self):
        print(f"{self.nome} está comendo!")

class Cachorro(Animal):
    def __init__(self,nome):
        super().__init__(nome)
    def latir(self):
        print(f"{self.nome} está latindo!")

c1 = Cachorro("Caramelo")
c1.latir()
c1.comer()