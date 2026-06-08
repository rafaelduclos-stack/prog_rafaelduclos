class Forma:
    def area():
        return 0

class Triangulo(Forma):
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    def area(self):
        return (self.base*self.altura) / 2
    
class Quadrado(Forma):
    def __init__(self,lado):
        self.lado = lado
    def area(self):
        return self.lado * self.lado

formas = [
    Triangulo(6,7),
    Quadrado(10),
    Triangulo(8,15),
    Quadrado(4),
    Quadrado(7)
]

for i in formas:
    print(f"Área: {i.area()}")