km = int(input('A distância de sua viagem em Km: '))

preco = 0

if km <= 200:
    preco = km * 0.50
    print('Sua viagem irá custar: {:.2F}R$.'.format(preco))
else:
    preco = km * 0.45
    print('Sua viagem irá custar: {:.2F}R$'.format(preco))