

def opcao(msg):
    try:
        opc = int(input(msg))
        if opc > 3:
            print('     \033[31mX ERRO! Opção inválida. X\033[m')
        else:
            return opc
    except:
        print('     \033[31mX ERRO! Opção inválida. X\033[m')


def nome(msg):
    try:
        nome = str(input(msg))
        return nome
    except:
        print('       \033[31mX ERRO! Dado inválida. X\033[m')


def idade(msg):
    while True:
        try:
            idade = int(input(msg))
            return idade
        except:
            print('       \033[31mX ERRO! Digite um número inteiro válido. X\033[m')
