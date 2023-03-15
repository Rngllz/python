from random import randint, choice

nomes = ['','','','']

for i in range(len(nomes)):
    nomes[i] = input('Diga o nome do {}º aluno: '.format(i+1))

print('O aluno escolhido foi: {}.'.format(nomes[randint(0, 3)]))
print('O aluno escolhido foi: {}.'.format(choice(nomes)))
