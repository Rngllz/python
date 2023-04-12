# Meu código V V V

from random import sample
from time import sleep
c = int(input('\nQuantos jogos você quer que eu sorteie? '))

print('\n')
for v in range(1,c+1):
    sorteio = sample(range(1, 61), 6)
    sorteio.sort()
    print(f'Jogo {v}: {sorteio}')
    sleep(1)
print('\n')


# Código do professor V V V

from random import randint
lista = list()
jogos = list()
cont = 0

print('-'*30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-'*30)
quant = int(input('Quantos jogos você quer que eu sorteie: '))
tot = 1

while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break

    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

print('-='*3, f' SORTEANDO {quant} JOGOS ','-='*3)
for m, n in enumerate(jogos):
    print(f'Jogo {m+1}: {n}')
    sleep(1)
    print('-='*5, '< BOA SORTE! >', '-='*5)
