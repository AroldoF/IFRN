num=input("Digite um número: ")
new=''
for i in range(len(num)-1,-1,-1):
    new+=num[i]
print(new)