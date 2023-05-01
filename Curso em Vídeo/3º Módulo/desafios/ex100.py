from random import randint
num = list()


def sorteia(lst):
    print('Sorteando 5 valores da lista:',end=' ')
    for c in range(0,5):
        lst.append(randint(1,10))
        print(lst[c],end=' ')
    print('PRONTO!')


def somaPar():
    sorteia(num)
    soma = 0
    for n in num:
        if n%2 == 0:
            soma += n
    print(f'Somando os valores pares de {num}, temos {soma}')

print()
somaPar()
print()