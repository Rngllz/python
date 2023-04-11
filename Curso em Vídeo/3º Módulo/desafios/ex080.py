números = []
cont = 0
for c in range(0,5):
    cont += 1
    num = int(input('\033[m\nValor numérico: \033[32m'))
    print('Número inserido',end=' ')
    if cont == 1:
        números.append(num)        
        print('no final.')
        print(números)
    else:
        if num > números[-1]:
            números.append(num)
            print('no final.')
            print(números)
        else:
            for c in range(0,5):
                if num < números[c]:
                    números.insert(c,num)
                    print(f'na posição {c}.')
                    print(f'{números}\033[m')
                    break

# Código do professor

lista = []
for c in range(0,5):
    n = int(input('Digite um valor: '))
    print('Número inserido')
    if c == 0 or n > lista[-1]: # assim ficou melhor, menos código
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista): # achei o for mais eficiente
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {lista}')