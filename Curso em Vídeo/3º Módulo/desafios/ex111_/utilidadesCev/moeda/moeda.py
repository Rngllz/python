
#EX 111

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
    return f'R${n:.2f}'


def resumo(p,a,d):
    print('_'*35)
    print('‾'*35)
    print(f"{'RESUMO DO VALOR':^35}")
    print('_'*35)
    print('‾'*35)
    print(f"{'Preço analisado:':<20}{moeda(p)}")
    print(f"{'Dobro do preço:':<20}{dobro(p, True)}")
    print(f"{'Metade do preço:':<20}{metade(p, True)}")
    print(f"{str(a)+'% de aumento:':<20}{aumentar(p, a, True)}")
    print(f"{str(d)+'% de redução::':<20}{diminuir(p, d, True)}")
    print('_'*35)
    print('‾'*35)

