from os import system


class Loja:
    def __init__(self):
        self.categorias = []

    def criar_categoria(self, nome):
        nova_categoria = Categoria(nome)
        self.categorias.append(nova_categoria)

    def criar_produto(self, nome, preco, categoria_nome):
        for categoria in self.categorias:
            if categoria.nome == categoria_nome:
                novo_produto = Produto(nome, preco)
                categoria.produtos.append(novo_produto)
                return
        print(f"Categoria '{categoria_nome}' não encontrada!")


class Categoria:
    def __init__(self, nome):
        self.nome = nome
        self.produtos = []
    def aplicar_descontos(self,desconto):
        if 0<=desconto<=100:
            for produto in self.produtos:
                desconto_tot=(produto.preco*desconto)/100
                produto.preco-=desconto_tot
            print("Desconto Aplicado com sucesso!")

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def aplicar_descontos(self,desconto):
        if 0<=desconto<=100:     
            desconto_tot=(self.preco*desconto)/100
            self.preco-=desconto_tot
            print("Desconto Aplicado com sucesso!")

loja = Loja()
loja.criar_categoria("Eletrônicos")
loja.criar_categoria("Roupas")

loja.criar_produto("Celular", 1500, "Eletrônicos")
loja.criar_produto("Celular", 1500, "Eletrônicos")
loja.criar_produto("Camisa", 50, "Roupas")

while True:
    print("Digite 0 para sair\nDigite 1 para criar categorias\nDigite 2 para criar produtos\nDigite 3 para aplicar descontos\nDigite 4 para mostrar a lista de categorias")
    r = int(input("Digite um número:"))
    system("cls")
    match r:
        case 0:
            break
        case 1:
            loja.criar_categoria(input("Digite o nome da categoria: "))
        case 2:
            for j, i in enumerate(loja.categorias):
                print(f"{j+1} - {i.nome}")
            while True:
                r = int(input("Digite o número da categoria ou 0 para voltar: "))
                if r == 0:
                    break
                else:
                    nome = input("Digite o nome do produto: ")
                    preço = float(input("Digite o preço do produto: "))
                    loja.criar_produto(nome, preço, loja.categorias[r - 1].nome)
                    print(loja.categorias[r - 1].produtos)
        case 3:
            for i,categoria in enumerate(loja.categorias):
                    print(f"{i} | {categoria.nome}")
            esc=int(input("Digite a categoria escolhida: "))
            print('Digite se deseja aplicar o desconto em uma categoria ou em um produto:')
            desc=input("Sua decisão: [C/P] ")
            if desc[0] in 'Cc':
                desconto = int(input("Digite a porcentagem de desconto que deseja aplicar ao produto: "))
                loja.categorias[esc].aplicar_descontos(desconto)
            elif desc[0] in 'Pp':
                for i,produto in enumerate(loja.categorias[esc].produtos):
                    print(f"{i} | {produto.nome} - {produto.preco:.2f}")
                p=int(input("Digite o categoria escolhida: "))
                desconto = int(input("Digite a porcentagem de desconto que deseja aplicar ao produto: "))
                loja.categorias[esc].produtos[p].aplicar_descontos(desconto)
            else:
                print("Erro!")
        case 4:
            print("Lista de Categorias:")
            for i in loja.categorias:
                print(f"{i.nome}:")
                if not i.produtos:
                    print("     Não há produtos cadastrados nessa categoria!")
                else:
                    for j in i.produtos:
                        print(f"     {j.nome} - {j.preco:.2f}")
    print()
