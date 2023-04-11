matriz = [[[],[],[]],[[],[],[]],[[],[],[]]]
pares = t_c = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor [{l},{c}]: '))
        if matriz[l][c]%2 == 0:
            pares += matriz[l][c]

print()
for l in range(0,3):
    for c in range(0,3):
        print(matriz[l][c], end='    ')
    print('\n')

print(f'A soma de todos os valores pares é: {pares}')
print(f'A soma de todos os valores da terceira coluna é:',end=' ')
for l in range(0,3):
    t_c += matriz[l][2]
print(t_c)
print(f'O maior valor da segunda linha é: {max(matriz[1])}\n')