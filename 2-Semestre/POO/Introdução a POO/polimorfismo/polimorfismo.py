class animal():
    def __init__(self):
        self.nome=''
        self.som=''
    def emitir_som(self):
        print(f'{self.nome} - {self.som}')

class cachorro(animal):
    def __init__(self):
        super().__init__()
        self.nome='Cachorro'
        self.som='Au Au'

class gato(animal):
    def __init__(self):
        super().__init__()
        self.nome='gato'
        self.som="Miau"

class vaca(animal):
    def __init__(self):
        super().__init__()
        self.nome='vaca'
        self.som="Muu"
            
dog=cachorro()
dog.emitir_som()
cat=gato()
cat.emitir_som()
caw=vaca()
caw.emitir_som()