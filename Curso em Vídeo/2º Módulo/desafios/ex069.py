sexo = ''
maior = homens = mu20 = 0
while True:
    print('\n'+'\033[33m-'*25)
    idade = int(input("\033[mIdade: \033[32m"))
    if idade >= 18:
        maior += 1
    #while sexo 'MF':
    sexo = str(input("\033[mSexo [M/F]: \033[32m")).strip().upper()[0]
    if sexo == 'M':
        homens += 1
    else:
        if idade < 20:
            mu20 += 1
    r = str(input("\033[m\nContinar [S/N]: \033[32m")).strip().upper()[0]
    print('\033[33m-'*25)    
    if r == 'N':
        break
print('\n'+'\033[32m='*35)
print(f'\033[mForam cadastradas {maior} maiores de 18 anos.\nForam registrados {homens} homens.\nForam registrados {mu20} mulheres com menos de 20 anos.')
print('\033[32m='*35)
print('\033[m')