lista = list()
for i in range(0, 16):
    lista.append(i)
print(lista[1:10])
print(lista[8:14])
print(lista[::2])
print(lista[1::2])
print(f"multiplos de 2: {lista[2::2]}")
print(f"multiplos de 3: {lista[2::3]}")
print(f"multiplos de 4: {lista[2::4]}")
lista.sort(reverse=True)
print(f"Lista na ordem decrescente: {lista}")
lista.sort()
soma = 0
somaf =0.0
for i in range(10, 16):
    soma = soma + i
for i in range(3,10):
    somaf= somaf +i
print(soma,somaf)
print(soma/somaf)
for i in lista:
    print (i)