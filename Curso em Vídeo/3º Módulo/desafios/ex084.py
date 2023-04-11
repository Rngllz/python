dados = list()
pessoas = list()
pesado = leve = 0
r = ' '
while r != 'N':
    
    dados.clear()
    dados.append(str(input('\n\nNome: ')))
    dados.append(int(input('Peso (Kg): ')))
    pessoas.append(dados[:])

    if len(pessoas) == 1:
        pesado = leve = dados[1]
    else:
        if dados[1] > pesado:
            pesado = dados[1]
        if dados [1] < leve:
            leve = dados[1]

    r = ' '
    while r not in 'SN':
        r = str(input('\nContinuar [S/N]: ')).strip().upper()[0]

print(f'\n\nForam cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi de {pesado}kg:',end=' ')
for p in pessoas:
    if p[1] == pesado:
        print(p[0],end='; ')
print(f'\nO menor peso foi de {leve}kg:',end=' ')
for p in pessoas:
    if p[1] == leve:
        print(p[0],end='; ')    
print()
