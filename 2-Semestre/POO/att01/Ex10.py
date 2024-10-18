from random import randint

num= randint(0,100)
while True:
    jogador=int(input("Tente adivinhar o número: "))
    if jogador<num:
        print(f'{jogador} foi um bom chute! Mas pq não tenta um número mais alto!')
    elif jogador==num:
        print(f'muito bem! {num} é o número correto')
        break
    else:
        print(f'{jogador} foi um bom chute! Mas pq não tenta um número mais baixo!')