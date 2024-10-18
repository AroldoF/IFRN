while True:    
    num = input("Digite um número: ")
    if num[-1] in '0':
        break
soma = 0
for i in num:
    soma = soma + int(i)
print(soma)
