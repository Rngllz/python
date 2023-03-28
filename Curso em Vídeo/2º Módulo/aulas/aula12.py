nome = str(input('Digite seu nome: '))

if nome == 'Luca': # Simples
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria': # Aninhada
    print('Seu nome é bem popular no Brasil!')
elif nome == 'José' or nome == 'Marcos':
    print('Nome muito top.')
else: # Composta
    print('Mas que nome comum...')

print('Tenha um bom dia {}.'.format(nome))