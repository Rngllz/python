lista = ('Lápis','1.75','Borracha','2.00','Caderno','15.90','Estojo','25.00','Transferidor','4.20','Compasso','9.99','Mochila','120.32','Canetaa','22.30','Livro','34.90')

print('\n'+'\033[34m-'*50)
print('\033[36m{:^50}'.format('LISTAGEM DE PREÇOS'))
print('\033[34m-'*50)
for c in range(0,len(lista)):
    if c%2 == 0:
        print('\033[33m{:.<40}\033[32mR$'.format(lista[c]),end='')
    else:
        print('{:>8}'.format(lista[c]))
print('\033[34m-'*50)
print('\033[m')