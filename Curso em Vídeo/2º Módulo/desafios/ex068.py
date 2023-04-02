from random import randint
soma = 0
vitórias = 0
robo = randint(1,10)
# 0 = par
# 1 = ímpar
while True:
    print('\n'+'\033[33m='*50)
    valor = int(input("\033[mDigite um valor: "))
    pessoa = str(input("Escolha par ou ímpar: ")).strip().upper()[0]
    soma = robo + valor
    if soma%2 == 0:
        if pessoa == 'P':
            print(f'\nO computador escolheu {robo}, você {valor}. A soma deu {soma} (PAR)')
            print('Parabéns você ganhou!!!\nVamos jogar novamente...')
            print('\033[33m='*50)
            vitórias += 1
        else:
            print(f'\nO computador escolheu {robo}, você {valor}. A soma deu {soma} (PAR)')
            print('Você \033[31mPERDEU!\033[m Ruim demais.')
            print('\033[33m='*50)
            break
    else:
        if pessoa == 'Í':
            print(f'\nO computador escolheu {robo}, você {valor}. A soma deu {soma} (ÍMPAR)')
            print('Parabéns você ganhou!!!\nVamos jogar novamente...')
            print('\033[33m='*50)
            vitórias += 1
        else:
            print(f'\nO computador escolheu {robo}, você {valor}. A soma deu {soma} (ÍMPAR)')
            print('Você \033[31mPERDEU!\033[m Ruim demais.')
            print('\033[33m='*50)
            break       
print('\n'+'\033[32m-'*35)
print(f'Você obteve {vitórias} vítorias consecutivas!')
print('-'*35)
print('\033[m')