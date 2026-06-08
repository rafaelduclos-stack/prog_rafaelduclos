class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def desconto(self, desconto):
        print(self.preco-(self.preco*(desconto/100)))

p1 = Produto("Teclado",300.0)
p1.desconto(67.0)