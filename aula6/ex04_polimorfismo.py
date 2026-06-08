class Pagamento:
    def processar(valor):
        return valor
    
class Dinheiro(Pagamento):
    def processar(valor):
        return valor - (valor*0.05)

class Cartao(Pagamento):
    def processar(valor):
        return valor + (valor*0.02)
    
class Pix(Pagamento):
    pass
    
print(Dinheiro.processar(100.0))
print(Cartao.processar(100.0))
print(Pix.processar(100.0))