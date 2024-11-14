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

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

loja = Loja()
while True:
    r=int(input("Digite um número:"))
    if r==1:
        loja.criar_categoria(input("Digite o nome da categoria: "))
    elif r==2:
        for j,i in enumerate(loja.categorias):
            print(f"{j+1} - {i.nome}")
        while True:
            r=int(input("Digite o número da categoria ou 0 para voltar: "))
            if r==0:
                r=1
                break
            else:
                print("Digite 1 para criar um produto:")
                p=int(input("Digite sua ação: "))
                if p==1:
                    nome=input("Digite o nome do produto: ")
                    preço=int(input("Digite o preço do produto: "))
                    loja.criar_produto(nome,preço,loja.categorias[r - 1].nome)
                    print(loja.categorias[r-1].produtos)
                elif p==2:
                    desconto=int(input("Digite a quantidade desconto: "))

    elif r==0:
        break

# Exemplo de uso
loja.criar_categoria("Eletrônicos")
loja.criar_categoria("Roupas")

loja.criar_produto("Celular", 1500, "Eletrônicos")
loja.criar_produto("Camisa", 50, "Roupas")

# Exibindo categorias e produtos
for categoria in loja.categorias:
    print(f"Categoria: {categoria.nome}")
    for produto in categoria.produtos:
        print(f"  Produto: {produto.nome}, Preço: R${produto.preco:.2f}")
