from classe_veiculo import veículos

class moto(veículos):
    def __init__(self, marca, modelo, ano, tipoGuidao):
        super().__init__(marca, modelo, ano)
        self.tipoGuidao = tipoGuidao

    def exibirDetalhes(self):
        super().exibirDetalhes()
        print(f"O tipo de Guidao é {self.tipoGuidao}")