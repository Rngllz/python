
tupla = (int(input('Digite um valor: ')),int(input('Digite um valor: ')),int(input('Digite um valor: ')),int(input('Digite um valor: ')))

print('')
print(tupla)
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
print(f'A primeira aparição do valor 3 foi na {tupla.index(3)+1}ª posição' if (tupla.count(3)) != 0 else 'O valor 3 não foi digitado')
print('Os únicos valores pares: ',end='')
for c in tupla:
    if c%2 == 0:
        print(c,end=' ')