def soma(a,b):
    print(f'A = {a}\nB = {b}')
    s = a + b
    print(f'a soma é: {s}')
    

soma(4,5)
soma(b=7,a=6)
soma(74,45)
soma(48,59)

print()


# DESENPACOTAMENTO 
def contador(*num):
    for valor in num:
        print(f'{valor}',end=', ')
    print()

contador(2,4,5)
contador(7,40,5,9,8,3)


def soma_tudo(*num):
    a = 0
    for c in num:
        a += c
    print(a)

soma_tudo(8,5,5,12,)
soma_tudo(22)

####################


valores = [2,6,4,2,1,6,78]


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


print(valores)
dobra(valores)
print(valores)