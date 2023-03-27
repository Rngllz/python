num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
num3 = int(input('Terceiro número: '))

#if (num1 > num2) and (num1 > num3):
#    print('O primeiro número, {}, é maior que o segundo e terceiro; {}, {}.'.format(num1, num2, num3))
#elif (num2 > num1) and (num2 > num3):
#    print('O segundo número, {}, é maior que o primeiro e terceiro; {}, {}.'.format(num2, num1, num3))
#else:
#    print('O terceiro número, {}, é maior que o primeiro e segundo; {}, {}.'.format(num3, num1, num2))

menor = num1
maior = num1

if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num2

if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

print('O menor número é o {}.\nO maior número é o {}.'.format(menor,maior))