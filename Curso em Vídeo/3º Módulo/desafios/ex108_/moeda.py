
#EX 108

def metade(n):
    r = n / 2
    return r
    

def dobro(n):
    r = n * 2
    return r


def aumentar(n,porc):
    r = n + (n * porc / 100)
    return r


def diminuir(n,porc):
    r = n - (n * porc / 100)
    return r



def moeda(n):
    return f'R${n:.2f}'.replace('.',',')

