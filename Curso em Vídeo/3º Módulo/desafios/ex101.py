from datetime import datetime
anoAtual = datetime.now().year


def voto(ano):
    """
    -> Verifica se a pessoa pode votar ou não
    :param ano: Anos de nascimento da pessoa
    :return: Se a pessoa é obrigada a votar, opcional ou negada.
    """
    idade = anoAtual - ano
    print(f'   .Com {idade} anos:',end=' ')
    if idade < 16:
        print('NEGADO')
    elif (18 > idade >= 16) or ( idade > 65):
        print('OPCIONAL')
    else:
        print('OBRIGATÓRIO')

anoNasc = int(input('   .Informe seu ano de nascimento: '))
voto(anoNasc)

help(voto)