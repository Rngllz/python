
# MEU CÓDIGO


def contador(inicio,fim,passo):
    if passo == 0:
        passo = 1
    if inicio > fim:
        if passo >= 0:
            passo *= -1
    print()
    print(f'- Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}')
    print(' ',end=' ')
    for n in range(inicio,fim,passo):
        print(n,end=' ')
    print(f'FIM')

contador(1,10,1)
contador(10,0,-2)
print()
print(' Contagem personalizada')
inicio = int(input(' -Início: '))
fim = int(input(' -Fim: '))
passo = int(input(' -Passo: '))
contador(inicio,fim,passo)

print()



# CÓDIGO DO PROFESSOR


from time import sleep


def contador2(i,f,p):

    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    print('-='*20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    cont = i
    sleep(2.5)


    if i < f:
        while cont <= f:
            print(f'{cont}',end=' ', flush=True)
            sleep(0.5)
            cont += p
    else:   
        while cont >= f:
            print(f'{cont}',end=' ',flush=True)
            sleep(0.5)
            cont -= p
    print('FIM')


contador2(1,10,1)
contador(10,0,2)
print()
print('Agora é sua vez d epersonalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini,fim,pas)