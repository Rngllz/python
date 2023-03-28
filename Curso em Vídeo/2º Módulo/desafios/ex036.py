valor = float(input('Qual o \033[30m valor \033[m da casa: '))
salario = float(input('Informe o seu \033[32m salário \033[m: '))
anos = int(input('Em quantos \033[34m anos \033[m pretende pagar: '))

if valor / anos > 30 * salario / 100:
    print('\033[41m Seu empréstimo foi negado.\033[m')
else:
    print('\033[42m Seu empréstimo foi aceito. \033[m')