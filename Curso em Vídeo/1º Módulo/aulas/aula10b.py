n1 = float(input('Diga a primeira nota: '))
n2 = float(input('Diga a segunda nota: '))

media = (n1 + n2)/2

print('A sua média foi {:.1f}'.format(media))

print('boa média' if media > 6 else 'estude mais')

if media < 6:
    print('Você foi reprovado')
elif media == 6:
    print('Você está de recuperação')
elif media > 6:
    print('Você foi aprovado')