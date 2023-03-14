from math import sqrt, ceil, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz quadrade de {} é {:.2f}\nArredondado para cima ficará: {}\nArredondado para baixo ficará: {}'.format(num, raiz, ceil(raiz), floor(raiz)))