
#EX 112

# Meu código:

def leiaDinheiro(msg):
    while True:
        v = str(input(msg)).strip()

        if v.isnumeric():
            return int(v.strip())
        elif v.replace(',','',1).isnumeric():
            return float(v.replace(',','.',1).strip())
        elif v.replace('.','',1).isnumeric():
            return float(v.strip())
        else:
            print(f'ERRO: "{v}" é um preço inválido.')


# Código do professor:

def leiaDinheiro2(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
        else:
            válido = True
            return float(entrada)