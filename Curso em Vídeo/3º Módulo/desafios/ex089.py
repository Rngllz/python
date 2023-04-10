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