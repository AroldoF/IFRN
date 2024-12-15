class Pessoa():
    def __init__(self, nome='', idade=0, peso=0.0, altura=0.0):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def envelhecer(self):
        self.idade += 1
        if self.idade > 21:
            print("Essa pessoa não cresce mais!!")
        else:
            self.altura += 0.5

    def engordar(self):
        self.peso += float(input(f"Quantos kg {self.nome} engordou? "))
        return self.peso

    def emagrecer(self):
        self.peso -= float(input(f"Quantos kg {self.nome} emagreceu? "))

    def crescer(self):
        if self.idade > 21:
            print("Essa pessoa não cresce mais!!")
        else:
            self.altura += 0.5

    def mostrar_atributos(self):
        print(f"\nNome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Peso: {self.peso:.2f} kg")
        print(f"Altura: {self.altura:.2f} m\n")


# Lista para armazenar várias pessoas
pessoas = []

# Função para criar uma nova pessoa e adicionar à lista
def criar_pessoa():
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade: "))
    peso = float(input("Digite o peso: "))
    altura = float(input("Digite a altura: "))
    pessoa = Pessoa(nome, idade, peso, altura)
    pessoas.append(pessoa)
    print(f"{nome} foi adicionada à lista.")

# Menu de interação com vários objetos
while True:
    r = int(input("\nDigite 1 para criar uma nova pessoa, 2 para selecionar uma pessoa, ou 0 para sair: "))
    
    if r == 1:
        criar_pessoa()  # Cria e adiciona uma nova pessoa à lista
    
    elif r == 2:
        if len(pessoas) == 0:
            print("Nenhuma pessoa cadastrada.")
        else:
            # Mostra a lista de pessoas e permite selecionar uma delas
            print("\nPessoas cadastradas:")
            for i, pessoa in enumerate(pessoas):
                print(f"{i}: {pessoa.nome}")

            escolha = int(input("Selecione o número da pessoa: "))
            
            if 0 <= escolha < len(pessoas):
                pessoa_selecionada = pessoas[escolha]
                while True:
                    acao = int(input(f"\nO que deseja fazer com {pessoa_selecionada.nome}? \n1. Envelhecer\n2. Engordar\n3. Emagrecer\n4. Crescer\n5. Mostrar Atributos\n0. Voltar ao menu anterior\n: "))
                    
                    if acao == 1:
                        pessoa_selecionada.envelhecer()
                    elif acao == 2:
                        pessoa_selecionada.engordar()
                    elif acao == 3:
                        pessoa_selecionada.emagrecer()
                    elif acao == 4:
                        pessoa_selecionada.crescer()
                    elif acao == 5:
                        pessoa_selecionada.mostrar_atributos()
                    elif acao == 0:
                        break
            else:
                print("Seleção inválida.")
    
    elif r == 0:
        break
print(pessoas)