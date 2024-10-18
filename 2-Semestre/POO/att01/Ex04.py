num=int(input("Digite um número: "))
primo=True
for i in range(2,num):
    if num%i==0:
        primo=False
        print("Não é primo")
        break
if primo:
    print(f"O número {num} é primo!!!")