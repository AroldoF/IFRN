class Corrida:
    def __init__(self, distancia_total, vencedor='Nenhum'):
        self.distancia_total = distancia_total
        self.vencedor = vencedor
        self.lista_de_carros = list()

    def adicionar_carro(self):
        marca = input("Digite a marca: ").strip().title()
        modelo = input("Digite o modelo: ").strip().title()
        velocidade_atual = 0.0
        velocidade_maxima = float(input("Digite a velocidade máxima: "))
        tanque_combustivel = float(input("Digite o tamanho do tanque de combustível: "))
        consumo_combustivel = float(input("Digite o consumo de combustível (litros/km): "))
        
        # Cria uma instância de carro e adiciona à lista de carros
        car = Carro(marca, modelo, velocidade_atual, velocidade_maxima, tanque_combustivel, consumo_combustivel)
        self.lista_de_carros.append(car)

class Carro:
    def __init__(self, marca, modelo, velocidade_atual, velocidade_maxima, tanque_combustivel, consumo_combustivel):
        self.marca = marca
        self.modelo = modelo
        self.velocidade_atual = velocidade_atual
        self.velocidade_maxima = velocidade_maxima
        self.tanque_combustivel = tanque_combustivel
        self.consumo_combustivel = consumo_combustivel
    def acelerar(self,quantidade):
        if self.velocidade_maxima>=self.velocidade_atual+quantidade:
            self.velocidade_atual+=quantidade
        else:
            print("Esse carro já chegou na velocidade máxima!")
    def frear(self,quantidade):
        if 0<=self.velocidade_atual-quantidade:
            self.velocidade_atual-=quantidade
        else:
            print("Esse carro esta parado!")
    def abastecer(self,litros):
        self.tanque_combustivel+=litros
    def dirigir(self,distancia):
        if distancia*self.consumo_combustivel<=self.tanque_combustivel:
            self.tanque_combustivel-=distancia*self.consumo_combustivel
        else:
            print("Essa carro não tem combustivel para percorrer essa distância")
    def verificar_combustivel(self):
        print(self.tanque_combustivel)
    def status(self):
        print(self.marca)
        print(self.modelo)
        print(self.velocidade_atual)
        print(self.tanque_combustivel)
# Criação de uma corrida
corrida1 = Corrida(100)

# Adiciona carros na corrida
corrida1.adicionar_carro()
corrida1.adicionar_carro()
while True:
    for i,carro in enumerate(corrida1.lista_de_carros):
        print(f"{i}: {carro.marca}")
    r=int(input("Escolha um carro: "))
    while True:
        p=int(input("Escolha uma ação: "))
        if p==1:
            quantidade=float(input("Digite a quantidade que Km/h que você deseja acelerar: "))
            corrida1.lista_de_carros[r].acelerar(quantidade)
        elif p==2:
            quantidade=float(input("Digite a quantidade que Km/h que você deseja frear: "))
            corrida1.lista_de_carros[r].frear(quantidade)
        elif p==3:
            quantidade=float(input("Digite a quantidade de litros que deseja reabastecer: "))
            corrida1.lista_de_carros[r].abastecer(quantidade)
        elif p==4:
            quantidade=float(input("Digite a quantidade de km que deseja percorrer: "))
            corrida1.lista_de_carros[r].dirigir(quantidade)
        elif p==5:
            corrida1.lista_de_carros[r].verificar_combustivel()
        elif p==6:
            corrida1.lista_de_carros[r].status()
        elif p==0:
            break