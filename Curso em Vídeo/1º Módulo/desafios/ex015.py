km = float(input('Distância percorrida: km'))
dia = int(input('Quantidade de dias alugado: d'))
preco = (km*0.15) + (dia*60)
print('O valor a ser pago pelo aluguel do carro é: {:.2f}R$'.format(preco))