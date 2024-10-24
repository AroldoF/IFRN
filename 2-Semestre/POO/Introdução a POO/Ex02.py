class pessoas():
    nome=''
    idade=0
    peso=0.0
    altura=0.0
    def envelhecer(self):
    self.idade+=1
    if self.idade>21:
        print("Essa pessoa não crece mais!!")
    else:
        self.altura+=0.5
    def engordar(self):
    self.peso+=float(input("Quantos kg você engordou? "))
    return self.peso
    def emagrecer(self):
    self.peso-=float(input("Quantos kg você emagreceu? "))
    def crescer(self):
    if self.idade>21:
        print("Essa pessoa não crece mais!!")
    else:
        self.altura+=0.5
def criar_pessoa():
    nome=input("Digite seu nome: ")
    idade=int(input("Digite sua idade: "))
    peso=float(input("digite seu peso: "))
    altura=float(input("digite sua altura: "))
    pessoa=pessoas(nome,idade,altura,)

lista=[]
while True:
    r=int(input(": "))
    #if r==9:

    if r==1:
        envelhecer(p1)
        print(p1.idade)
        print(p1.altura)
    elif r==2:
        engordar(p1)
        print(p1.peso)
    elif r==3:
        emagrecer(p1)
        print(p1.peso)
    elif r==4:
        crescer(p1)
        print(p1.altura)
    elif r==0:
        break