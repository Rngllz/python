
# Meu código

from time import sleep

def maior(*num):
    lst = list()
    print()
    print(' Analisando os valores passados...')
    print(' ',end='')

    for c in num:
        print(c,end=' ', flush=True)
        lst.append(c)
        sleep(0.4)
    if len(lst) == 0:
        lst.append(0)

    print(f'Foram informados {len(num)} valores ao todo.')
    print(f' O maior valor informado foi o {max(lst)}.')
    print()


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()



# Código do professor

def maior2(*num):
    cont = maior = 0
    print('-='*30)
    print('Analisando os valores passados... ')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior vlaor informado foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()