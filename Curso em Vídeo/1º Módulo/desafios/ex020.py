from random import sample

alun = ['A','B','C','D']


for i in range(0,3):
    alun[sample(range(0,3),3)] = input('Nome: ')
    print(alun[i])
