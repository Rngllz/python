import numpy as np
soma = 0
matriz = np.array([[3, 4, 1],
                   [3, 1, 9]])

for l in range(matriz.shape[0]):
    for c in range(matriz.shape[1]):
        soma += matriz[l][c]

print(f'O resultado é: {soma}')