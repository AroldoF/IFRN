from classe_veiculo import veículos

class carro(veículos):
    def __init__(self, marca, modelo, ano, numeroPortas):
        super().__init__(marca, modelo, ano)
        self.numeroPortas = numeroPortas

    def exibirDetalhes(self):
        super().exibirDetalhes()
        print(f"O número de Portas é {self.numeroPortas}")