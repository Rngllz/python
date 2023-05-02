def fatorial(num):
    f = 1
    for c in range(num, 0 , -1):
        f *= c
    return f

n = int(input('Digite um número: '))
print(f'O fatorial é: {fatorial(n)}.')



def par(n):
    if n%2 == 0:
        return True
    else:
        return False
    
num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')



def mult(a,b):
    '''
        -> Faz a multiplicação entre 'a' e 'b'
        :param a: valor que multiplica o 'b'
        :param b: valor a ser multiplicado pelo 'a'
        :return: o resultado da multiplicação
    '''
    r = a * b
    return r

print(mult(4,5))

help(mult)