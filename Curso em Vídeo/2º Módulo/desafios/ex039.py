from datetime import datetime,date
from dateutil import relativedelta

ano = int(input('Ano do nascimento: '))
mes = int(input('Mês do nascimento: '))
dia = int(input('Dia do nascimento: '))


diferenca_an = relativedelta.relativedelta(datetime.now(),datetime(ano,mes,dia))
diferenca_18 = relativedelta.relativedelta(datetime.now(),datetime(ano+18,mes,dia))

if diferenca_an.years > 18:
    print('Já passou da hora de ter se alistado.')
    print('Já se passaram {} ano(s), {} mês(es) e {} dia(s).'.format(diferenca_18.years, diferenca_18.months, diferenca_18.days))

elif diferenca_an.years == 18:
    print('Está na hora de se alistar.')

else:     
    print('Você ainda vai se alistar.')
    print('Faltam {} ano(s), {} mês(es) e {} dia(s)'.format(abs(diferenca_18.years), abs(diferenca_18.months), abs(diferenca_18.days)))
