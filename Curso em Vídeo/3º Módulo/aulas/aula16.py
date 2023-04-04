lanche = ('Hambúrguer','Suco', 'Pizza', 'Pudim')
print(lanche[-4])
print(lanche[0::2])
# ERRADO -> lanche[1] = 'Olá'
print(lanche[:3])

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer um {comida}, posição {pos}')

for cont in range(0,len(lanche)):
    print(f'Vou comer um {lanche[cont]}')