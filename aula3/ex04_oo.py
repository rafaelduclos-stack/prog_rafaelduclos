class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def depositar(self, valor):
        self.saldo+=valor
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo-=valor
        else:
            print("Saldo insuficiente")
    def extrato(self):
        print(f"Titular: {self.titular} | Saldo:R${self.saldo} ")

conta1 = ContaBancaria("Rafael Duclos",100000000.0)
conta1.depositar(67)
conta1.sacar(50000)
conta1.extrato()