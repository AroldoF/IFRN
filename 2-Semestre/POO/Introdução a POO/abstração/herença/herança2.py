class ContaBancaria:
    def __init__(self, titular, numero_conta):
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R$ {valor} realizado com sucesso.')
        else:
            print('Valor de depósito inválido.')

    def sacar(self, valor):
        if valor <= 0:
            print('Valor de saque inválido.')
            return

        if valor > self.saldo:
            print('Saldo insuficiente.')
        else:
            self.saldo -= valor
            print(f'Saque de R$ {valor} realizado com sucesso.')

    def exibir_saldo(self):
        print(f'Saldo da conta {self.numero_conta} de {self.titular}: R$ {self.saldo:.2f}')


class ContaCorrente(ContaBancaria):
    def __init__(self, titular, numero_conta):
        super().__init__(titular, numero_conta)
        self.limite_credito = 1000

    def sacar(self, valor):
        if valor <= 0:
            print('Valor de saque inválido.')
            return

        if valor > self.saldo + self.limite_credito:
            print('Saldo insuficiente, inclusive com o limite de crédito.')
        else:
            # Subtrai o valor do saque e aplica a taxa de 2%
            taxa = valor * 0.02
            valor_total = valor + taxa
            self.saldo -= valor_total
            print(f'Saque de R$ {valor} realizado com sucesso, com uma taxa de R$ {taxa:.2f}.')

    def exibir_saldo(self):
        print(f'Saldo da conta corrente {self.numero_conta} de {self.titular}: R$ {self.saldo:.2f}')


class ContaPoupanca(ContaBancaria):
    def __init__(self, titular, numero_conta):
        super().__init__(titular, numero_conta)

    def aplicar_rendimento(self, taxa):
        if taxa > 0:
            rendimento = self.saldo * (taxa / 100)
            self.saldo += rendimento
            print(f'Apliquei rendimento de {taxa}%: R$ {rendimento:.2f}.')
        else:
            print('Taxa de rendimento inválida.')

    def exibir_saldo(self):
        print(f'Saldo da conta poupança {self.numero_conta} de {self.titular}: R$ {self.saldo:.2f}')


class ContaSalario(ContaBancaria):
    def __init__(self, titular, numero_conta):
        super().__init__(titular, numero_conta)
        self.saques_realizados = 0

    def sacar(self, valor):
        if self.saques_realizados >= 1:
            print('Você já fez um saque este mês. Não é permitido mais de um saque por mês.')
        else:
            if valor <= 0:
                print('Valor de saque inválido.')
                return
            if valor > self.saldo:
                print('Saldo insuficiente.')
            else:
                self.saldo -= valor
                self.saques_realizados += 1
                print(f'Saque de R$ {valor} realizado com sucesso.')

    def exibir_saldo(self):
        print(f'Saldo da conta salário {self.numero_conta} de {self.titular}: R$ {self.saldo:.2f}')


# Função de teste do sistema
def testar_sistema():
    # Instanciando contas com dados fictícios
    conta1 = ContaCorrente('João Silva', '001')
    conta2 = ContaPoupanca('Maria Oliveira', '002')
    conta3 = ContaSalario('Carlos Pereira', '003')

    # Realizando depósitos
    conta1.depositar(1500)
    conta2.depositar(2000)
    conta3.depositar(3000)

    # Realizando saques
    conta1.sacar(500)  # Deve ser possível, já que tem limite de crédito
    conta1.sacar(1200)  # Com taxa de 2% sobre o valor

    conta2.sacar(500)  # Saque simples
    conta2.aplicar_rendimento(5)  # Aplicando rendimento de 5%

    conta3.sacar(1000)  # Saque válido
    conta3.sacar(500)  # Tentativa de saque adicional

    # Exibindo saldos finais
    conta1.exibir_saldo()
    conta2.exibir_saldo()
    conta3.exibir_saldo()

# Testando o sistema
testar_sistema()
