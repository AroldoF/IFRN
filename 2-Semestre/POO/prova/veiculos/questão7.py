from classe_carro import carro
from classe_moto import moto

moto_nova = moto("honda", "bros", "2024", "C")
carro_velho = carro("fiat", "uno", "2003", 4)
print("Detalhes tecnicos da moto:")
moto_nova.exibirDetalhes()
print()
print("Detalhes tecnicos do carro:")
carro_velho.exibirDetalhes()
