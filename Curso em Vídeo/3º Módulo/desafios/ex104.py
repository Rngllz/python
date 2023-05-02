
# Meu código

a = False

def leiaInt(msg):
    """
    -> Verifica se o valor é um número válido
    Args:
        msg (str): Mensagem que aparecerá no input

    Returns:
        str: Retorna o número, caso ele for válido
    """
    global a
    valor = str(input(msg))
    if valor.strip().isnumeric():
        a = True
        return valor.strip()
    else:
        print('\033[31mERRO! Digite um número inteiro válido.\033[m\n')

while a == False:
    n = leiaInt('Digite um número: ')
print(f'\033[32mVocê acabou de digitar o número {n}.\033[m')


# Código do professor

def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor

num = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')