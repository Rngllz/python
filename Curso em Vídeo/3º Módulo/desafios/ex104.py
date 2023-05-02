
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
        print('ERRO! Digite um número inteiro válido.\n')

while a == False:
    n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')