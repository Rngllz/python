msg = ''


def responsivo(txt,cor):
    tm = len(txt.strip())
    
    print(f'\033[{cor}m    '+'~'*(tm+10))
    print(f'    {txt.strip():^{tm+10}}')
    print('    '+'~'*(tm+10) + f'\033[m')




while True:
    print()
    responsivo('-SISTEMA DE AJUDO PyHELP-',"34")
    msg = str(input('    .Função ou Biblioteca > '))
    if msg == 'fim':
        responsivo(f"ENCERRANDO O SISTEMA","31")
        break
    else:
        print()
        responsivo(f"Acessando o manual do comando '{msg}'","32")
        help(msg)
        print(msg.__doc__)
    