from random import shuffle, choice

pessoas = ["maria", "Rosa", "João", "José", "Roberta", "Michael", "P.Dydy"]
print(pessoas)
print(f"A pessoa escolhida foi {choice(pessoas)}!")
shuffle(pessoas)
print(pessoas)
print(f"A pessoa escolhida foi {choice(pessoas)}!")

nome=input("Digite um nome: ").upper()
print(f"O nome de trás para frente fica: {nome[::-1]}")