tupla = ('termo','audio','olhar','vitoria','cachorro')
print('\n')
for c in range(0,len(tupla),1):
    print(f"\033[mA palavra '{tupla[c]}' possui as seguintes vogais:",end=' ')
    for d in tupla[c]:
        if d in 'AaEeIiOoUu':
            print('\033[32m{}'.format(d),end=' ')
    print('\n')
print('\033[m\n')