from random import randint
aleatorios = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
print('\n',aleatorios)
print(f' Maior: {sorted(aleatorios)[-1]}')
print(f' Menor: {sorted(aleatorios)[0]}\n')

# Forma do professor:

print(f' Maior: {max(aleatorios)}')
print(f' Menor: {min(aleatorios)}\n')
