from ex115_.verificacoes import verificacoes

info = list()
cores = {'Verde':'\033[32m',
         'Vermelho':'\033[31m',
         'Tira':'\033[m'}

def placa(msg):
    print('     '+'-'*45)
    print('     '+msg.center(45))
    print('     '+'-'*45)


def menu_principal():
    print()
    placa('MENU PRINCIPAL')
    print(f'     {cores["Verde"]}.1 -{cores["Tira"]} Ver pessoas cadastradas')
    print(f'     {cores["Verde"]}.2 -{cores["Tira"]} Cadastrar novas Pessoas')
    print(f'     {cores["Verde"]}.3 -{cores["Tira"]} Sair do Sistema')
    
    print('     '+'-'*45)
    opc = verificacoes.opcao(f'     Sua Opção: {cores["Verde"]}')
    print(cores["Tira"])

    return opc


def novo_cadastro():
    print()
    placa('NOVO CADASTRO')
    nome = verificacoes.nome(f'      .Nome: {cores["Verde"]}')
    print(cores["Tira"])
    idade = verificacoes.idade(f'      .Idade: {cores["Verde"]}')
    print(cores["Tira"])

    with open("desafios/ex115_/txt/bd.txt", "r", encoding="utf-8") as arquivo:
        info = arquivo.readlines()

    info.append(nome+'-'+str(idade)+' anos\n')

    with open("desafios/ex115_/txt/bd.txt", "w", encoding="utf-8") as arquivo:
        for num in range(len(info)):
            arquivo.write(info[num])

    print(f'       {cores["Verde"]}* Novo registo de {nome} adicionado. *{cores["Tira"]}')

    
def pessoas_cadastradas():
    print()
    placa('PESSOAS CADASTRADAS')

    with open("desafios/ex115_/txt/bd.txt", "r", encoding="utf-8") as arquivo:
        info = arquivo.readlines()

    for pessoa in info:
        teste = pessoa.split('-')
        print(f'      .{teste[0]}\t\t{teste[1]}',end='')


'''
        OUTRA FORMA DE MANIPULAR ARQUIVOS DE TEXTO


        a = open(arquivo.txt, 'wt+')
                               write text (+ é caso o arquivo ainda não exista)    

        a = open(arquivo.txt, 'rt')
                               read text

        a = open(arquivo.txt, 'at')
                               append text

        a.read()
        a.readlines()
        a.close()
        a.write('askdalskd')

'''