file = open("POO/leitura.txt", "r")
linhas = file.readlines()
file.close()
arquivo = open("POO/escrita.txt", "w")
for i in linhas:
    arquivo.write(i)
    arquivo.write("\n")
arquivo.close()
print("Seu arquivo foi lido e salvo em escrita.txt com quebra de linhas!")
