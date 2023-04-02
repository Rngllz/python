from random import randint

robo = randint(0,10)
pessoa = 0
tentativa = 0

print("\033[33\nmEu pensei em um número de 0 a 10\nTente adivinhar!\033[m")
while pessoa != robo:
    tentativa += 1
    pessoa = int(input("\nDigite um número: "))
    if pessoa != robo:
        if pessoa > robo:
            print("\033[31mMenos",end='')
        else:
            print("\033[31mMais",end='')
        print(", tente novamente!\033[m")

print("\033[32mParabêns!! O número que o robô escolheu era {}\nVocê acertou em {} tentativas!\033[m".format(robo,tentativa))