class Instrumento():
    def tocar(self):
        print("Som de instrumento genérico")
    
class Violao(Instrumento):
    def tocar(self):
        print("Som acústico")

class Piano(Instrumento):
    def tocar(self):
        print("Som de piano")

class Bateria(Instrumento):
    def tocar(self):
        print("Som de percurssão")

instrumentos = [
    Violao(),
    Piano(),
    Bateria()
]

for i in instrumentos:
    i.tocar()