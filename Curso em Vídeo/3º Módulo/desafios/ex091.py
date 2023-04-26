from time import sleep
from random import sample
dici = dict()
lista = list()
lista_2 = list()

num = sample(range(1, 6), 4)

for c in range(0,4):
    dici['jogador'] = 'jogador'+str(c+1)
    dici['jogo'] = num[c]
    lista.append(dici.copy())

print('Valores Sorteados')
for c in lista:
    print(f'   O {c["jogador"]} tirou {c["jogo"]}')
    sleep(1)

for b in range(0,4):
    lista_2.append(lista[b]['jogo'])
lista_2.sort(reverse=True)


print('Ranking dos Jogadores')
for b in range(0,4):
    print(f'   {b+1}º lugar:',end=' ')
    for b2 in range(0,4):
        if lista[b2]['jogo'] == lista_2[b]:
            print(f'{lista[b2]["jogador"]} com {lista_2[b]}')
    sleep(1)