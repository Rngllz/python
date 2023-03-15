nome_completo = str(input('Diga seu nome completo: ')).strip()

n = nome_completo.split()

print('Primeiro nome: {}\nÚltimo nome: {}'.format(n[0], n[-1]))
print('Último nome: {}.'.format(n[len(n)-1]))
