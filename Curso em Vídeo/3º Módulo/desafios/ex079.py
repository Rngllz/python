números = []
num = 0
while True:
    num = (int(input('\n\033[mDigite um número: \033[32m')))
    if num not in números:
        print('Número cadastrado!')
        números.append(num)
        print(números)
    else:
        print(f'\033[31mO NÚMERO {num} JÁ ESTÁ CADASTRADO!!!\033[m')
    
    r = ' '
    while r not in 'NS':
        r = str(input('\033[mContinuar [S/N]: \033[32m')).strip().upper()[0]
    if r == 'N':
        break
números.sort()
print(f'\n\033[33mOs valores cadastrados foram: {números}\033[m\n')