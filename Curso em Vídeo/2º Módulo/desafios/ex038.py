num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))

if num1 > num2:
    print('O primeiro número, {}, é maior que o segundo, {}.'.format(num1,num2))
elif num2 > num1:
    print('O segundo número, {}, é maior que o primeiro, {}.'.format(num2,num1))
else:
    print('Os números possuem o mesmo valor.')
