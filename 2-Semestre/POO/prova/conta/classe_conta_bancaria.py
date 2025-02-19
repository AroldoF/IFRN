class ContaBancaria:
    def __init__(self,titular, saldo, numeroConta):
        self.titular=titular
        self.saldo=saldo
        self.numeroConta=numeroConta
    def depositar(self,valor):
        if valor>0:
            self.saldo+=valor
        else:
            print("Valor Invalido!")
    def sacar(self,valor):
        if valor<self.saldo and valor>0:
            self.saldo-=valor
        else:
            print("Valor Invalido!")
    def exibirSaldo(self):
        print(f"Seu saldo é {self.saldo}")