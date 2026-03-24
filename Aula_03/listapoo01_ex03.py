class ContaBancaria:
    def __init__(self):
        self.titular = ""
        self.numero = ""
        self.saldo = 0
    def depositar(self, v):
        self.saldo += v
    def sacar(self, v):
        self.saldo -= v    

x = ContaBancaria()
x.titular = "Eduardo"
x.numero = "123-X"
print(x.saldo)
x.depositar(100)
print(x.saldo)
x.sacar(20)
print(x.saldo)

