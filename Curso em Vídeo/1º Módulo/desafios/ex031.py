km = int(input('A distância de sua viagem em Km: '))
preco = 0

#if km <= 200:
#    preco = km * 0.50
#else:
#    preco = km * 0.45

preco = km * 0.50 if km <= 200 else km * 0.45

print('Sua viagem irá custar: R${:.2F}'.format(preco))
