from ntpath import join


nome_completo = input('Diga seu nome completo: ')
nome = nome_completo.split()
print('Seu nome com todas as letras maiúsculas é: {}.'.format(nome_completo.upper()))
print('Seu nome com todas as letras minúsculas é: {}.'.format(nome_completo.lower()))
print('Seu nome possui {} letras.'.format(len(''.join(nome_completo.split()))))
print('Seu primeiro nome possui {} letras.'.format(len(nome[0]))) 
print('Seu primerio nome possui {} letras.'.format(nome_completo.find(' ')))