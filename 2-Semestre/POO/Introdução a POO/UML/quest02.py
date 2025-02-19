class Produto:
    def __init__(self, codigo, valor, descricao):
        self.__codigo = codigo
        self.__valor = valor
        self.__descricao = descricao

    def get_valor(self):
        return self.__valor

    def get_descricao(self):
        return self.__descricao

    def get_codigo(self):
        return self.__codigo

# Lista global para armazenar os produtos cadastrados
lista_produtos = []

class Pedido:
    def __init__(self):
        self.__valor_total = 0.0
        self.lista_de_itens = []

    def adicionar_item(self, itemPedido):
        self.lista_de_itens.append(itemPedido)
        self.__valor_total += itemPedido.get_valor_total()

    def get_total(self):
        return self.__valor_total

# Lista global para armazenar os pedidos realizados
lista_pedidos = []

class ItemPedido:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def get_valor_total(self):
        return self.produto.get_valor() * self.quantidade

    def get_detalhes(self):
        return {
            "produto": self.produto.get_descricao(),
            "quantidade": self.quantidade,
            "valor_total": self.get_valor_total()
        }

