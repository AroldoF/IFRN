class ContaBancaria:
    def __init__(self,titular,numero_conta,saldo):
        self.titular=titular
        self.numero_conta=numero_conta
        self.saldo=saldo
    def depositar(self,valor):
        if valor > 0:
            self.saldo+=valor
        else:
            print('Valor de depósito inválido.')
    def sacar(self,valor):
        if(valor>self.saldo):
            print(f"O valor {valor} que você deseja retirar e maior que seu saldo {self.saldo}!!!")
            if self.saldo>0:
                r=input("Você deseja retirar todo o seu saldo? [S/N] ")
                if r[0] in 'Ss':
                    self.saldo-=self.saldo
                    print('Seu saque foi concluido!')
                else:
                    print('Seu saque não foi concluido!')
            else:
                print("Saldo Zerado")
        else:
            self.saldo-=valor
            print('Seu saque foi concluido!')
    def exibir_saldo(self):
        print(f"Seu saldo: {self.saldo}")
class ContaCorrente(ContaBancaria):
    def __init__(self, titular, numero_conta, saldo):
        super().__init__(titular, numero_conta, saldo)
        self.limite_credito = 1000
    def sacar(self, valor):
        #return super().sacar(valor)
        if valor > self.saldo + self.limite_credito:
            print('Saldo insuficiente, inclusive com o limite de crédito.')
        else:
            # Subtrai o valor do saque e aplica a taxa de 2%
            taxa = valor * 0.02
            valor_total = valor + taxa
            self.saldo -= valor_total
            print(f'Saque de R$ {valor} realizado com sucesso, com uma taxa de R$ {taxa:.2f}.')
# conta=ContaBancaria('Gui','999898678',258.7)
# conta.sacar(20)
# conta.exibir_saldo()
