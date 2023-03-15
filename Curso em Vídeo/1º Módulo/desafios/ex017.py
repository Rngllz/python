from math import pow, hypot
c_oposto = float(input('O valor do cateto oposto: '))
c_adjacente = float(input('O valor do cateto adjacente: '))

hipotenusa = pow(pow(c_oposto, 2) + pow(c_adjacente, 2), 0.5)
print('A hipotenusa do triângulo retângulo é: {:.2f}'.format(hipotenusa))
print('A hipotenusa vai medir {:.2f}'.format(hypot(c_oposto, c_adjacente)))
