km = int(input('Diga a quantos km/h você estava dirigindo: '))

if km <= 80:
    print('Tudo certo então...')
else:
    print('Você foi multado! Sua multa: {:.2f}R$'.format((km - 80)*7))