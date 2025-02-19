from abc import ABC

class Operacoes(ABC):
    def adicionar():
        pass
    def remover():
        pass
class ListaOperacoes(Operacoes):
    def __init__(self):
        self.lista_numeros=[]
    def adicionar(self,num):
        self.lista_numeros.append(num)
    def remover(self,num):
        self.lista_numeros.remove(num)
    def listar(self):
        for i in self.lista_numeros:
            print(i, end=' ')
        print()

numeros=ListaOperacoes()
numeros.adicionar(9)
numeros.adicionar(4)
numeros.remover(4)
numeros.listar()