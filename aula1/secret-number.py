import random

rand = random.randint(1, 5)

userNum = int(input('Escolha um número entre 1 e 5: '))

if userNum == rand:
    print('Acertou, miserável!')
else:
    print('Errou, numero correto = ', rand)
