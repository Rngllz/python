
def ler():
    return float(input('Temperatura em Celsius: '))


def calcula(C):
    return (9 * C + 160) / 5


def mostra(F):
    print(f'A temperatura em Fahrenheit é: {F}')


mostra(calcula(ler()))