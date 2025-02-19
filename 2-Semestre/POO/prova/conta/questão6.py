from classe_conta_bancaria import ContaBancaria

lista_contas=[]

def Mostrar_contas():
    for i,conta in enumerate(lista_contas):
        print(f"{i} | {conta.titular}")
        
conta=ContaBancaria('Aroldo',0,'9187421')
lista_contas.append(conta)

while True:
    print("Digite 1 para criar uma conta\nDigite 2 para uma conta existente")
    escolha=int(input("Digite sua escolha: "))
    match escolha:
        case 0:
            break
        case 1:
            titular=input("Digite o nome do titular: ")  
            numeroConta=input("Digite o número da conta: ")
            conta=ContaBancaria(titular,0,numeroConta)
            lista_contas.append(conta)
            print("Conta criada com sucesso!")
        case 2:
            while True:
                print("0 para voltar\n1 para depositar\n2 para sacar\n3 para mostar seu saldo")
                escolha=int(input("Digite sua escolha: "))
                match escolha:
                    case 0:
                        break
                    case 1:
                        Mostrar_contas()
                        pessoa=int(input("Digite a conta que dejesa usar: "))
                        valor=float(input("Digite o valor a ser depositado: "))
                        lista_contas[pessoa].depositar(valor)
                    case 2:
                        Mostrar_contas()
                        pessoa=int(input("Digite a conta que dejesa usar: "))
                        valor=float(input("Digite o valor a ser sacado: "))
                        lista_contas[pessoa].sacar(valor)
                    case 3:
                        Mostrar_contas()
                        pessoa=int(input("Digite a conta que dejesa usar: "))
                        lista_contas[pessoa].exibirSaldo()