class veículos:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibirDetalhes(self):
        print(f"A marca é {self.marca}")
        print(f"A modelo é {self.modelo}")
        print(f"A ano é {self.ano}")