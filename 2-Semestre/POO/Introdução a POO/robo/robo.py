class Caminho():
    def __init__(self,vago,bomba,comida):
        self.vago=vago
        self.bomba=bomba
        self.comida=comida
        self.player=False
        self.aparencia=' + '
    def bombas(self):
        self.vago=False
        self.bomba=True
    def  player_troca(self):
        self.vago=False
        self.player=True
    def comida_troca(self):
        self.vago=False
        self.comida=True
linha=list()
coluna=list()
for i in range(0,20):
    for j in range(0,20):
        caminho=Caminho(True,False,False)
        coluna.append(caminho)
    linha.append(coluna[:])
    coluna.clear()
linha[0][0].bombas()
for i in linha:
    for k,j in enumerate(i):
        if k%20==0:
            print()
        if j.vago:
            print(f"\033[32m{j.aparencia}\033[m", end='')
        elif j.bomba:
            print(f"\033[35m{j.aparencia}\033[m", end='')
        elif j.comida:
            print(f"\033[37m{j.aparencia}\033[m", end='')