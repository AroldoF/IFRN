from random import shuffle, choice

numeros01 = list()
numeros02 = list()
for i in range(0, 10):
    numeros01.append(i)
    numeros02.append(i)

shuffle(numeros01)
shuffle(numeros02)
i = 0

while True:
    num_int = choice(numeros01)
    num_str = str(num_int)
    num_int = choice(numeros02)
    num_str = str(num_int) + num_str
    if num_str in '00':
        continue
    else:
        print(num_str)
    if i == 9:
        break
    i = i + 1
