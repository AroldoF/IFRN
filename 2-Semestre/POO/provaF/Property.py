from abc import ABC, abstractmethod

class Propriedade(ABC):
    def __init__(self,espaco_construido,num_quartos,num_banheiros):
        self.__espaco_construido=espaco_construido
        self.__num_quartos=num_quartos
        self.__num_banheiros=num_banheiros

    def get_espaco_construido(self):
        return self.__espaco_construido
    
    def set_espaco_construido(self,new_espaco_construido):
        self.__espaco_construido=new_espaco_construido

    def get_num_quartos(self):
        return self.__num_quartos
    
    def set_num_quartos(self,new_num_quartos):
        self.__num_quartos=new_num_quartos

    def get_num_banheiros(self):
        return self.__num_banheiros
    
    def set_num_banheiros(self,new_num_banheiros):
        self.__num_banheiros=new_num_banheiros

    #@abstractmethod   
    def __str__(self):
        return f'''Informações sobre a Propriedade:\n
    O espaço contruido é {self.__espaco_construido}m²!
    Número de quartos é {self.__num_quartos}!
    Número de banheiros é {self.__num_banheiros}!'''

    def display(self):
        print(self)

    @abstractmethod
    def indice_aproveitamento(self):
        pass

class Casa(Propriedade):
    def __init__(self, espaco_construido, num_quartos, num_banheiros,garagem,quintal):
        super().__init__(espaco_construido, num_quartos, num_banheiros)
        if(garagem):
            self.__garagem="possui garagem"
        else:
            self.__garagem="não possui garagem"
        if(quintal):
            self.__quintal ="possui quintal"
        else:
            self.__quintal="não possui quintal"
        self.status_do_imovel='Desocupado!'
        self.metodo=None
            
    def mudança_status(self,metodo):
        self.metodo=metodo 
        if(metodo.status=='Comprar'):
            self.status_do_imovel='Comprado'
            nome=input("Insira o nome do comprador:").strip()
            metodo.realizar_compra(nome)
        elif(metodo.status=='Alugar'):
            self.status_do_imovel='Alugado'
            nome=input("Insira o nome quem vai alugar:").strip()
            metodo.alugar(nome)

    def get_garagem(self):
        return self.__garagem
    
    def set_garagem(self,new_garagem):
        if(new_garagem):
            self.__garagem="possui garagem"
        else:
            self.__garagem="não possui garagem"

    def get_quintal(self):
        return self.__quintal
    
    def set_quintal(self,new_quintal):
        if(new_quintal):
            self.__quintal ="possui quintal"
        else:
            self.__quintal="não possui quintal"

    def __str__(self):
        return super().__str__()+f'''
    A propriedade {self.__garagem}
    A propriedade {self.__quintal}
    O status do propriedade é {self.status_do_imovel}'''

    def display(self):
        return super().display()
    
    def indice_aproveitamento(self):
        return (self.__num_quartos+self.__num_banheiros)/self.__espaco_construido

class Apartamento(Propriedade):
    def __init__(self, espaco_construido, num_quartos, num_banheiros,varanda,andar):
        super().__init__(espaco_construido, num_quartos, num_banheiros)
        if(varanda):
            self.__varanda="possui varanda"
        else:
            self.__varanda="não possui varanda"
        self.__andar=andar
        self.status_do_imovel='Desocupado!'
        self.metodo=None

    def mudança_status(self,metodo):
        self.metodo=metodo 
        if(metodo.status=='Comprar'):
            self.status_do_imovel='Comprado'
            nome=input("Insira o nome do comprador:").strip()
            self.metodo.realizar_compra(nome)
        elif(metodo.status=='Alugar'):
            self.status_do_imovel='Alugado'
            nome=input("Insira o nome quem vai alugar:").strip()
            self.metodo.alugar(nome)

    def get_varanda(self):
        return self.__varanda
    
    def set_varanda(self,new_varanda):
        if(new_varanda):
            self.__varanda="possui varanda"
        else:
            self.__varanda="não possui varanda"

    def get_andar(self):
        return self.__andar
    
    def set_andar(self,new_andar):
        self.__andar=new_andar

    def __str__(self):
        return super().__str__()+f'''
    A propriedade {self.__varanda}
    Está no {self.__andar}° andar
    O status do propriedade é {self.status_do_imovel}'''

    def display(self):
        return super().display()
    
    def indice_aproveitamento(self):
        return (self.__num_quartos+self.__num_banheiros)/self.__espaco_construido

class Hotel(Propriedade):
    def __init__(self, espaco_construido, num_quartos, num_banheiros,andares,elevador):
        super().__init__(espaco_construido, num_quartos, num_banheiros)
        self.__andares=andares
        if(elevador):
            self.__elevador="possui elevador"
        else:
            self.__elevador="não possui elevador"
        self.status_do_imovel='Desocupado!'
        self.metodo=None

    def mudança_status(self,metodo):
        self.metodo=metodo 
        if(metodo.status=='Comprar'):
            self.status_do_imovel='Comprado'
            nome=input("Insira o nome do comprador:").strip()
            metodo.realizar_compra(nome)

    def get_andares(self):
        return self.__andares
    
    def set_andares(self,new_andares):
        self.__andares=new_andares

    def get_elevador(self):
        return self.__elevador
    
    def set_elevador(self,new_elevador):
        if(new_elevador):
            self.__elevador="possui elevador"
        else:
            self.__elevador="não possui elevador"

    def __str__(self):
        return super().__str__()+f'''
    São {self.__andares} andares
    A propriedade {self.__elevador}
    O status do propriedade é {self.status_do_imovel}'''

    def display(self):
        return super().display()
    
    def indice_aproveitamento(self):
        #'andares - 1' porque desconsiderei o térreo
        return ((self.__num_quartos+self.__num_banheiros)*(self.__andares-1))/self.__espaco_construido

class Alugavel():
    def __init__(self,mobiliado,preco):
        self.status='Alugar'
        if(mobiliado):
            self.__mobiliado="é mobiliado"
        else:
            self.__mobiliado="não é mobiliado"
        self.__preco=preco
    def get_mobiliado(self):
        return self.__mobiliado
    def set_mobiliado(self,new_mobiliado):
        if(new_mobiliado):
            self.__mobiliado="é mobiliado"
        else:
            self.__mobiliado="não é mobiliado"
    def get_preco(self):
        return self.__preco
    def set_preco(self,new_preco):
        self.__preco=new_preco
    def alugar(self,nome_do_inquilino):
        print(f"alugado pelo valor de R$ {self.__preco} para {nome_do_inquilino}")
    def __str__(self):
        return f'''Sobre o Aluguel:\n
    A propriedade {self.__mobiliado}.
    O preço é {self.__preco}R$.'''
    def info(self):
        print(self)

class Compravel():
    def __init__(self,taxas,preco):
        self.status='Comprar'
        self.__taxas=taxas
        self.__preco=preco
    def get_taxas(self):
        return self.__taxas
    def set_taxas(self,new_taxas):
        self.__taxas=new_taxas
    def get_preco(self):
        return self.__preco
    def set_preco(self,new_preco):
        self.__preco=new_preco
    def realizar_compra(self,nome_do_comprador):
        print(f"comprado pelo valor de R$ {self.__preco} para o comprador {nome_do_comprador}")
    def __str__(self):
        return f'''Sobre a Compra:\n
    A taxa é {self.__taxas}.
    O preço é {self.__preco}R$.'''
    def info(self):
        print(self)

