def leiaInt(msg):
    while True:
        try:
            n = str(input(msg))
            if n == '':
                n = 0
                print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            i = int(n)
        except:
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        else:
            return i

def leiaReal(msg):
    while True:
        try:
            n = str(input(msg))
            if n == '':
                n = 0
                print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            i = int(n)
        except:
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
        else:
            return n