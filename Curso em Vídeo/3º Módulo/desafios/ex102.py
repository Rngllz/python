
def fatorial(num,show=False):
    """
    -> Traz o valor do fatorial de um número
    Args:
        num (int): número escolhido
        show (bool, optional): define se o cálculo será mostrado ou não. Defaults to False.
    """
    r = 1
    print()
    for c in range(num,0,-1):
        r *= c

    if show:
        for c in range(num,1,-1):
            print(c,end=' x ')
        print('1 =',end=' ')
    print(r)



fatorial(5,True)
fatorial(5,True)

print()