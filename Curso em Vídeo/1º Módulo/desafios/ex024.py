cidade = str(input('Digite o nome de uma cidade: ')).strip()

if((cidade.upper())[0:5] == ('SANTO') or (cidade.upper())[0:5] == ('SANTA')):
    print('Sua cidade possui o nome de um santo(a).')
else:
    print('Sua cidade não possui o nome de um santo(a).')

if(('SANTO' in cidade.upper()) or ('SANTA' in cidade.upper()) or ('SÃO' in cidade.upper())):
    print('Sua cidade possui o nome de um santo(a).')
else:
    print('Sua cidade não possui o nome de um santo(a).')