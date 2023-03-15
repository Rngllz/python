from random import sample, shuffle

nomes = ['','','','']
cont = 0

for i in range(0,4):
    nomes[i] = input('{}º Nome: '.format(i+1))

print(22*'-')

for i in sample(range(0,4),4):
    cont += 1
    print('{}º a apresentar é o {}'.format(cont, nomes[i]))

shuffle(nomes)
print('A ordem de apresentação será: {}'.format(nomes))

