valores = []
print('\n')
for v in range(0,5):
    valores.append(int(input(f'  \033[34m(posição {v})\033[m - \033[33m{v+1}º\033[m Número: \033[32m')))

maior = max(valores)
menor = min(valores)

print(f'\n  \033[mO maior valor foi \033[32m{maior}\033[m, na posição:', end=' ')
for c in range(0,len(valores)):
    if valores[c] == maior:
        print(f'\033[34m{c}\033[m - (\033[33m{c+1}º\033[m número)', end=' ')


print(f'\n  \033[mO menor valor foi \033[32m{menor}\033[m, na posição', end=' ')
for c in range(0,len(valores)):
    if valores[c] == menor:
        print(f'\033[34m{c}\033[m - (\033[33m{c+1}º\033[m número)', end=' ')
print('\n')