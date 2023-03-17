salario = float(input('Informe o seu salário: '))

if salario > 1250:
    salario = salario + (10 * salario)/100
    print('O seu salário terá um aumento de 10%, total: {}'.format(salario))
else:
    salario = salario + (15 * salario)/100
    print('O seu salário terá um aumento de 15%, total: {}'.format(salario))