lista = list()
c = soma = 0

for i in range(1,6):
    lista.append(int(input(f'Digite o {i}º valor: ')))

for n in lista:
    c += 1

    print(f'{n}',end=' ')
    soma += n
    
    if c != 5:
        print('+',end=' ')
    else:
        print(f'= {soma}')
