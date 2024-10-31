from os import system


class Corrida:
    def __init__(self, distancia_total, vencedor="Nenhum"):
        self.distancia_total = distancia_total
        self.vencedor = vencedor
        self.lista_de_carros = list()

    def adicionar_carro(self):
        marca = input("Digite a marca: ").strip().title()
        modelo = input("Digite o modelo: ").strip().title()
        velocidade_atual = 0.0
        velocidade_maxima = float(input("Digite a velocidade máxima: "))
        tanque_combustivel = float(input("Digite o tamanho do tanque de combustível: "))
        consumo_combustivel = float(
            input("Digite o consumo de combustível (litros/km): ")
        )

        # Cria uma instância de carro e adiciona à lista de carros
        car = Carro(
            marca,
            modelo,
            velocidade_atual,
            velocidade_maxima,
            tanque_combustivel,
            consumo_combustivel,
        )
        self.lista_de_carros.append(car)


class Carro:
    def __init__(
        self,
        marca,
        modelo,
        velocidade_atual,
        velocidade_maxima,
        tanque_combustivel,
        consumo_combustivel,
    ):
        self.marca = marca
        self.modelo = modelo
        self.velocidade_atual = velocidade_atual
        self.velocidade_maxima = velocidade_maxima
        self.tanque_combustivel = tanque_combustivel
        self.consumo_combustivel = consumo_combustivel
        self.distancia_corrida=0.0

    def acelerar(self, quantidade):
        if self.velocidade_maxima >= self.velocidade_atual + quantidade:
            self.velocidade_atual += quantidade
        else:
            print("Esse carro não pode acelerar tanto!")

    def frear(self, quantidade):
        if 0 <= self.velocidade_atual - quantidade:
            self.velocidade_atual -= quantidade
        else:
            print("Esse carro não pode frear tanto!")

    def abastecer(self, litros):
        self.tanque_combustivel += litros

    def dirigir(self, distancia):
        if distancia * self.consumo_combustivel <= self.tanque_combustivel:
            self.tanque_combustivel -= distancia * self.consumo_combustivel
            self.distancia_corrida+=distancia
            if self.distancia_corrida>=corrida1.distancia_total:
                corrida1.vencedor=self.modelo
                print(f'parabéns {self.modelo}, você ganhou a corrida!')
        else:
            print("Essa carro não tem combustivel para percorrer essa distância")

    def verificar_combustivel(self):
        print(self.tanque_combustivel)

    def status(self):
        print(f"A marca é {self.marca}")
        print(f"O modelo é {self.modelo}")
        print(f"A velocidade atual é {self.velocidade_atual}")
        print(f"A quantidade de combustível é {self.tanque_combustivel}")
        print(f"A quantidade de Km que o carro andou na corrida {self.distancia_corrida}")

# Criação de uma corrida
corrida1 = Corrida(100)

# Adiciona carros na corrida
while True:
    print("1 para criar um carro")
    print("2 para selecionar os carros")
    print("3 para ver a distancia em km da corrida")
    print("0 para finalizar")
    j = int(input("Digite uma ação: "))
    if j == 1:
        corrida1.adicionar_carro()
    elif j == 2:
        for i, carro in enumerate(corrida1.lista_de_carros):
            print(f"{i}: {carro.marca}")
        r = int(input("Escolha um carro: "))
        while True:
            print("1 para acelerar")
            print("2 para frear")
            print("3 para reabastecer")
            print("4 para dirigir")
            print("5 para verificar o combustível")
            print("6 para ver o status do carro")
            print("0 para retornar")
            p = int(input("Escolha uma ação: "))
            if p == 1:
                quantidade = float(
                    input("Digite a quantidade que Km/h que você deseja acelerar: ")
                )
                corrida1.lista_de_carros[r].acelerar(quantidade)
            elif p == 2:
                quantidade = float(
                    input("Digite a quantidade que Km/h que você deseja frear: ")
                )
                corrida1.lista_de_carros[r].frear(quantidade)
            elif p == 3:
                quantidade = float(
                    input("Digite a quantidade de litros que deseja reabastecer: ")
                )
                corrida1.lista_de_carros[r].abastecer(quantidade)
            elif p == 4:
                quantidade = float(
                    input("Digite a quantidade de km que deseja percorrer: ")
                )
                corrida1.lista_de_carros[r].dirigir(quantidade)
            elif p == 5:
                corrida1.lista_de_carros[r].verificar_combustivel()
            elif p == 6:
                corrida1.lista_de_carros[r].status()
            elif p == 0:
                break
            else:
                system('cls')
    elif j == 3:
        print(f"a quantidade de km totais da corrida é {corrida1.distancia_total} km")
    elif j == 0:
        break
    system("cls")
