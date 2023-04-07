num = []
par = []
impar = []
while True:
    num.append(int(input('\nDigite um número: ')))

    r = ' '
    while r not in 'SN':
        r = str(input('Continuar [S/N]: ')).strip().upper()[0]
    if r == 'N':
        break

print(f'\nA lista completa é: {num}')

for c in num:
    if c%2 == 0:
        par.append(c)
    else:
        impar.append(c)

print(f'A lista de pares é: {par}')
print(f'A lista de ímpares é: {impar}')
