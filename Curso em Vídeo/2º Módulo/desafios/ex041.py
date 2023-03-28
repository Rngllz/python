from datetime import date
#from dateutil import relativedelta

nasc = int(input('\nAno do nascimento: '))
#mes = int(input('Mês do nascimento: '))
#dia = int(input('Dia do nascimento: '))

atual = date.today().year
idade = atual - nasc

#idade = relativedelta.relativedelta(datetime.now(),datetime(ano,mes,dia))


print("\nVocê possui {} anos, sua classificação é: ".format(idade),end='')


if idade <= 9:
    print("\033[2;32mMIRIM\033[mn\n")
elif idade <= 14:
    print("\033[2;33mINFANTIL\033[m\n")
elif idade <= 19:
    print("\033[2;34mJUNIOR\033[m\n")
elif idade <= 20:
    print("\033[2;35mSENIOR\033[m\n")
else:
    print("\033[2;36mMASTER\033[m\n")
