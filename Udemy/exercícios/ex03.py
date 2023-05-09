idade = int(input('Sua idade: '))
print('Você é',end=' ')

if idade >= 0 and idade <= 12:
    print('Criança')
elif idade >= 13 and idade <= 18:
    print('Adolescente')
elif idade > 18:
    print('Adulto')
else:
    print('|| IDADE INVÁLIDA ||')