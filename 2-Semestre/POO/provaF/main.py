from Property import Casa,Apartamento,Hotel,Alugavel,Compravel,Propriedade
from Agente import Agente

teste=Agente()
casa=Casa(400,5,3,True,True)
aluguel=Alugavel(True,5000) 
print("A casa vai ser alugada:")
casa.mudança_status(aluguel)
teste.adicionar_propriedade(casa)

ap=Apartamento(50,2,1,9,6)
compra=Compravel(20,120000)
print("O apartamento sera vendido:")
ap.mudança_status(compra)
teste.adicionar_propriedade(ap)

ho=Hotel(1000,20,21,6,True)
comp=Compravel(40,1000000)
print("O hotel vai sem comprado:")
ho.mudança_status(compra)
teste.adicionar_propriedade(ho)

print("Informações sobre todos as Propriedades listada!")
teste.display_propriedades()

