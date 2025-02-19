class Agente():
    def __init__(self):
        self.__lista_de_propriedades=[]

    def adicionar_propriedade(self,Propriedade):
        self.__lista_de_propriedades.append(Propriedade)

    def remover_propriedade(self,Propriedade):
        self.__lista_de_propriedades.remove(Propriedade)

    def get_lista_de_propriedades(self):
        return self.__lista_de_propriedades
    
    def display_propriedades(self):
        for i in self.__lista_de_propriedades:
            i.display()
            print()

    def status_do_imovel(self,Propriedade):
        return [classe.__name__ for classe in Propriedade.metodo]