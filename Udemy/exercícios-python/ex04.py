m1 = float(input('1ª Nota: '))
m2 = float(input('2ª Nota: '))
m3 = float(input('3ª Nota: '))

media = round((m1+m2+m3)/3,1)
print(f'Média: {media}')

if media >= 0 and media <= 4.0:
    print(' -Aluno REPROVADO')
elif media >= 4.1 and media <= 6.0:
    print(' -Aluno está em EXAME')
    exame = float(input('  Nota do exame: '))
    if exame >= 6.0:
        print('  -Aluno APROVADO')
    else:
        print('  -Aluno REPROVADO')
else:
    print(' -Aluno APROVADO')