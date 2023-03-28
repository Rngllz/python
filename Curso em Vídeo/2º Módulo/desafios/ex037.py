
valor = int(input('Digite um número: '))
print('-=-'*6)
print('\033[32m 1 \033[m - Binário')
print('\033[33m 2 \033[m - Octal')
print('\033[34m 3 \033[m - Hexadecimal')
print('-=-'*6)
escolha = int(input('Opção para converter: '))

if escolha == 1:
    print('Binário')
elif escolha ==2:
    print('Octal')
else:
    print('Hexadecimal')
