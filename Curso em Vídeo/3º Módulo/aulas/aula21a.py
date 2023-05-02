help(print)
help(input)
# ou digitar 'help()' no prompt e depois o código


print(input.__doc__)
# explica mais sobre a documentação



# COMO FAZ UMA DOCSTRING
def contador(i, f, p):
    '''
        -> Faz uma contagem e mostra na tela.
        :param i: início da contagem
        :param f: fim da contagem
        :param p: passo da contagem
        :return: sem retorno
    '''
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')

contador(2, 10, 2)

help(contador)



# PARÂMETRO OPCIONAL
#             caso não venha nada pro c
#             ele adiciona o zero
#               v
def somar(a,b,c=0):
    s = a + b + c
    print(f'A soma vale {s}')

somar(3,2,5)
somar(8,4)



# ESCOPO DE VARIÁVEIS

def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


n = 2
print(f'No programa principal, o n vale {n}')
#print(f'Na função teste, x vale {x}') essa lihna não funcionaria pq o x é uma variável local,
#                                      diferente do n, que é uma variável global



def funcao():
    global n1
    n1 = 4 # Esse n1 foi criado como local
           # A única forma de usar uma váriavel global
           # é escrevendo o código 'global n1'
    print(f'N1 dentro vale {n1}')


n1 = 2
funcao()
print(f'N1 fora vale {n1}')



# RETORNANDO VALORES

def subtrair(a,b):
    s = a - b 
    return s

r1 = subtrair(3,2)
r2 = subtrair(2,2)
r3 = subtrair(5,6)

print(f'Resultados: {r1}, {r2}, {r3}')
