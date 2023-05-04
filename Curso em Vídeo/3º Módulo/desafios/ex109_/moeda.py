
#EX 109

def metade(n,b):
    r = n / 2
    if b == False:
        return r
    else:
        return moeda(r)
    

def dobro(n,b):
    r = n * 2
    if b == False:
        return r
    else:
        return moeda(r)


def aumentar(n,porc,b):
    r = n + (n * porc / 100)
    if b == False:
        return r
    else:
        return moeda(r)


def diminuir(n,porc,b):
    r = n - (n * porc / 100)
    if b == False:
        return r
    else:
        return moeda(r)


def moeda(n):
    return f'R${n:.2f}'.replace('.',',')
