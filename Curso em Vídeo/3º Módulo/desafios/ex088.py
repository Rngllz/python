from random import sample
from time import sleep
c = int(input('\nQuantos jogos você quer que eu sorteie? '))

print('\n')
for v in range(1,c+1):
    sorteio = sample(range(1, 61), 6)
    print(f'Jogo {v}: {sorteio}')
    sleep(1)
print('\n')