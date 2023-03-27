from random import randint

n = [0,1,2,3,4,5]
numero = n[randint(0,5)]

usu_n = int(input('Digite um número de 0 a 5: '))



if usu_n == numero:
    print('Parabêns você acertou o número!')
else:
    print('Poxa, você errrou, o número era {}.'.format(numero))
