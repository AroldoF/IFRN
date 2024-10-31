class Conta:
    def __init__(self, numero, titular, saldo, limite, codigo_Apo, nome_Apo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.codigo_Apo = codigo_Apo
        self.nome_Apo = nome_Apo

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        if self.saldo < valor:
            print("Você não tem saldo suficiente!")
            return False
        else:
            self.saldo -= valor
            return True

    def extrato(self): 
        print(f"Número: {self.numero}\nTitular: {self.titular}\nSaldo: {self.saldo}\nLimite: {self.limite}\nTipo de Conta: {self.nome_Apo}")

    def transferir(self, valor, conta_destino):
        if self.saca(valor):
            conta_destino.deposita(valor)
            print(f"Transferência de {valor} realizada para a conta {conta_destino.numero}.")
        else:
            print("Transferência não realizada devido a saldo insuficiente.")


numero1 = input("Digite o número da primeira conta: ")
titular1 = input("Digite o nome do titular da primeira conta: ")
saldo1 = float(input("Digite o saldo inicial da primeira conta: "))
limite1 = float(input("Digite o limite da primeira conta: "))
codigo_Apo1 = input("Digite o código da conta (01 para Corrente, 02 para Poupança): ")
nome_Apo1 = "Conta Corrente" if codigo_Apo1 == "01" else "Poupança"

conta1 = Conta(numero1, titular1, saldo1, limite1, codigo_Apo1, nome_Apo1)

numero2 = input("Digite o número da segunda conta: ")
titular2 = input("Digite o nome do titular da segunda conta: ")
saldo2 = float(input("Digite o saldo inicial da segunda conta: "))
limite2 = float(input("Digite o limite da segunda conta: "))
codigo_Apo2 = input("Digite o código da conta (01 para Corrente, 02 para Poupança): ")
nome_Apo2 = "Conta Corrente" if codigo_Apo2 == "01" else "Poupança"

conta2 = Conta(numero2, titular2, saldo2, limite2, codigo_Apo2, nome_Apo2)

valor_transferencia = float(input("Digite o valor a ser transferido da primeira conta para a segunda: "))
conta1.transferir(valor_transferencia, conta2)

print("\nExtrato da Primeira Conta:")
conta1.extrato()
print("\nExtrato da Segunda Conta:")
conta2.extrato()
