print('Hello World!')

IDADE = 17
NOME = 'Luca'
ALTURA = 1.81
VIVO = True

print(NOME.upper())
print(NOME.lower())
print(NOME.replace('ca','la'))

NUMEROS = []
NUMEROS.append(IDADE)
NUMEROS.append(ALTURA)
print(NUMEROS)

print(NOME)
NOME = input('Digite seu nome: ')
print(NOME)

VARIOS_NUMEROS = range(10,110,10)
IDADE = VARIOS_NUMEROS
print(list(VARIOS_NUMEROS))

for numero in VARIOS_NUMEROS:
    print(numero * 2)

for i in range (100,1000,20):
    print(i)