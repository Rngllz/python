sal = float(input('Valor do salário: '))
aum = int(input('Porcentagem de aumento: '))
print('O seu salário com {}% de aumento ficará: {:.2f}'.format(aum, sal + ((sal*aum)/100)))