valor = int(input('Digite um número: '))
print('-=-'*6)
print('\033[32m 1 \033[m - Binário')
print('\033[33m 2 \033[m - Octal')
print('\033[34m 3 \033[m - Hexadecimal')
print('-=-'*6)
escolha = int(input('Opção para converter: '))

if escolha == 1:
    print('{} convertido para BINÁRIO é igual a {}.'.format(valor, bin(valor)[2:]))
elif escolha ==2:
    print('{} convertido para OCTAL é igual a {}.'.format(valor, oct(valor)[2:]))
elif escolha == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(valor, hex(valor)[2:]))
else:
    print("\033[31mOPÇÃO INVÁLIDA!!!\033[m")
