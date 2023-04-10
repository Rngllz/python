matriz = [[[],[],[]],[[],[],[]],[[],[],[]]]

#linha
for l in range(0,3):
    #coluna
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor [{l},{c}]: '))


for l in range(0,3):
    for c in range(0,3):
        print(matriz[l][c], end='    ')
    print('\n')
#print(matriz[0])
#print(matriz[1])
#print(matriz[2])
    