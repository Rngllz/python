from time import sleep
msg = ''

def responsivo(txt,cor):
    """
    -> Método responsável por imprimir texto com detalhes resposnivos
    Args:
        txt (str): Contem o texto da mensagem
        cor (str): Define a cor que o textoe os detalhes irão possuir
    """
    tm = len(txt.strip()) + 10
    
    print(f'\033[{cor}m    '+'~'*(tm))
    print(f'    {txt.strip():^{tm}}')
    print('    '+'~'*(tm) + f'\033[m')



while True:
    print()
    sleep(1)
    responsivo('-SISTEMA DE AJUDO PyHELP-',"34")
    msg = str(input('    .Função ou Biblioteca > '))
    if msg == 'fim':
        responsivo(f"ENCERRANDO O SISTEMA","31")
        break
    else:
        print()
        sleep(.5)
        responsivo(f"Acessando o manual do comando '{msg}'","32")  
        sleep(2)
        help(msg)
        print(msg.__doc__)
    