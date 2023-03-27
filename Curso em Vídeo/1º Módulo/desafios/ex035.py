reta_1 = float(input('Primeira reta: '))
reta_2 = float(input('Segunda reta: '))
reta_3 = float(input('Terceira reta: '))

if (reta_1 > reta_2 - reta_3) and (reta_1 < reta_2 + reta_3):
    if (reta_2 > reta_1 - reta_3) and (reta_2 < reta_1 + reta_3):
        if (reta_3 > reta_1 - reta_2) and (reta_3 < reta_1 + reta_2):
            print('Com as medidas {}, {}, {}, pode sim ser formado um triângulo.'.format(reta_1, reta_2, reta_3))
        else:
            print('O terceiro valor, {}, não permite a criação de um triângulo.'.format(reta_3))
    else:
        print('O segundo valor, {}, não permite a criação de um triângulo.'.format(reta_2))
else:
    print('O primeiro valor, {}, não permite a criação de um triângulo.'.format(reta_1))