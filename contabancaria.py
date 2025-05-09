class contaBancaria:
    def __init__(self, saldo = 0):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"deposito de ${valor}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"saque de ${valor} realizado")
        else:
            ("saldo insuficiente")

acesso = contaBancaria()
acesso.depositar(valor=100)
acesso.sacar(valor=30)