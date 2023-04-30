jogador = dict()
gol = list()
partidas = 0

print()
jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
print()

for c in range(0,partidas):
     gol.append(int(input(f' - Quantos gols foram marcados na {c+1}ª partida? ')))
print()

jogador['gols'] = gol[:]
jogador['total'] = sum(gol)

print('-=-'*15)
for k,v in jogador.items():
     print(f' O campo {k} tem o valor {v}')
print('-=-'*15)
print()

print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for c,g in enumerate(gol):
     print(f'   => Na {c+1}ª partida, fez {g} gols.')

print()