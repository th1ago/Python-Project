class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Contruindo a conta")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("Saldo de {} do titular{}".format(self.saldo, self.titular))
    
    def deposita(self, valor):
        self.saldo += valor
    
    def saca(self, valor):
        self.saldo -= valor

conta = Conta(123, "Nico", 55.5, 1000.0)
print(conta.saldo)