km = int(input('Diga a quantos km/h você estava dirigindo: '))

if km <= 80:
    print('Tudo certo então...')
else:
    print('Você foi multado! Sua multa: {}R$'.format((km - 80)*7))