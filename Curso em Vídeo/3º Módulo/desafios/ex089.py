# Meu código

nome = list()
nota = list()
boletim = list()
aluno = list()
r = ' '
c = 0

while r != 'N':

    nome.clear()
    nota.clear()
    aluno.clear()

    nome.append(str(input('\n .Nome: ')))
    nota.append(float(input('   1ª nota: ')))
    nota.append(float(input('   2ª nota: ')))

    aluno.append(nome[:])
    aluno.append(nota[:])

    boletim.append(aluno[:])

    r = ' '
    while r not in 'SN':
        r = str(input(' Continuar [S/N]: ')).strip().upper()[0]

print(f"\n{'No.':<5} {'NOME':<15} {'MÉDIA':<10}")
print('-'*28)
for num, aluno in enumerate(boletim):
    print(f'{num:<5} {aluno[0][0]:<15} {sum(aluno[1])/2:<10}')
print('-'*28+'\n')

while True:
    c =  int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if c == 999:
        break
    print(f'As notas de {boletim[c][0][0]} são {boletim[c][1]}.\n')


# Código do professor

ficha = list()
while True:
    
    name = str(input('Nome: '))
    n1 = float(input('1ª Nota: '))
    n2 = float(input('2ª Nota: '))
    media = (n1 + n2)/2
    ficha.append([name,[n1,n2],media])

    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break

print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)

for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-'*35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe!): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')