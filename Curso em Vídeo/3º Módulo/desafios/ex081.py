números = []
cont = 0 
while True:
    números.append(int(input(f'\n\033[mDigite {cont+1}º número: \033[32m')))
    
    r = ' '
    while r not in 'SN':
        r = str(input('\033[mContinuar [S/N]: \033[32m')).strip().upper()[0]
    if r == 'N':
        break


print(f'\n\033[mForam cadastrados {len(números)} números.')
números.sort(reverse=True)
print(f'\033[mA lista ordenada de forma descrescente: {números}')
if 5 not in números:
    print('\033[mNão foi cadastrada nenhum número 5.')
else:
    print('\033[mO número 5 se encontra na posição: ',end=' ')
    for c in range(0,len(números)):
        if números[c] == 5:
            print(c,end='... ')
