temp = 0
valores = [[],[]]
for c in range(1,8):
    temp = int(input(f'Digite o {c}º número: '))
    if temp%2 == 0:
        valores[0].append(temp)
    else:
        valores[1].append(temp)
valores[0].sort()
valores[1].sort()
print(f'\nPares: {valores[0]}\nÍmpares: {valores[1]}\n')