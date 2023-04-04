
# Meu código

from math import trunc
cinquenta = vinte = dez = um = valor_2 = 0

valor = int(input("\nInsira o valor a ser sacado: \033[32m"))

cinquenta = trunc(valor / 50)
vinte = trunc((valor - (cinquenta * 50))/20)
dez = trunc(((valor - (cinquenta * 50)) - (vinte * 20))/10)
um = trunc(((valor - (cinquenta * 50)) - (vinte * 20) - (dez * 10))/1)

print('\n'+'\033[34m+=+'*6)
if cinquenta != 0:
    print(f'\033[33m{cinquenta}\033[m cédulas de \033[32mR$ 50')
if vinte != 0:
    print(f'\033[33m{vinte}\033[m cédulas de \033[32mR$ 20')
if dez != 0:
    print(f'\033[33m{dez}\033[m cédulas de \033[32mR$ 10')
if um != 0:
    print(f'\033[33m{um}\033[m cédulas de \033[32mR$ 1')
print('\033[34m+=+'*6)
print('\033[m')


# Código do professor

print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
cédula = 50
total_cédula = 0
while True:
    if total >= cédula:
        total -= cédula   # Ao mesmo tempo que ele desconta o valor da cédula
        total_cédula += 1 # ele conta, assim sabendo quantas cédulas poderam ser retiradas
    else:
        if total_cédula > 0:
            print(f'Total de {total_cédula} cédulas de R${cédula}') # mostra 
 
        if cédula == 50: # troca de cédulas
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1

        total_cédula = 0 # zera o total de cédulas usadas, para a próxima cédula começar do 0

        if total == 0:
            break # se todo o valor já foi descontado ent ele sai do loop