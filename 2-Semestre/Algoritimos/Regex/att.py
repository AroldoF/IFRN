from re import match, search
from os import system
from time import sleep


def validar_email(email):
    pattern = r"[a-zA-Z0-9._-]+\@[a-zA-Z-.]+\.[a-zA-Z]{2,}$"
    if match(pattern, email):
        return True
    else:
        return False


def validar_num(num):
    pattern = r"[-+]?[0-9]+[.,]?[0-9]*$"
    if match(pattern, num):
        return True
    else:
        return False


def validar_numero(num):
    #pattern = r"[0-9]{3}[-\s]?[0-9]{3}[-\s]?[0-9]{3}"
    pattern = r"[+]?[0-9]{2,3}[\s]?[(]?[0-9]{2}[)]?[\s]?[0-9]{4,5}[-.\s]?[0-9]{4}"
    if match(pattern, num):
        return True
    else:
        return False

while True:
    numero = str(input("Digite um texto: "))
    # email = str(input("Digite um texto: "))
    # print(f"Seu email é {validar_email(email)}")
    # print(f"Seu num é {validar_num(numero)}")
    print(f"Seu num é {validar_numero(numero)}")
    sleep(2)
    system("cls")
