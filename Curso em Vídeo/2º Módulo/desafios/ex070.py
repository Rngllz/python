n_barato = ''
total = mil = p_barato = c = 0
while True:
    c += 1
    print('\n'+'\033[33m+'*30)
    nome = str(input('\033[mNome: \033[32m'))
    preço = float(input('\033[mPreço: \033[32m'))
    total += preço
    if preço > 1000:
        mil += 1
    if c == 1:
        p_barato = preço
        n_barato = nome
    else:
        if preço < p_barato:
            p_barato = preço
            n_barato = nome
    r = str(input('\033[m\nContinuar [S/N]: \033[32m')).strip().upper()[0]
    print('\033[33m+'*30)
    if r == 'N':
        break
print('\n'+'\033[35m-'*35)
print(f'O total a ser pago é {total}.\n{mil} produtos custam mais que R$ 1000.\nO nome do produto mais barato (R$ {p_barato}) é: {n_barato}.')
print('\033[35m-'*35)
print('\033[m')
