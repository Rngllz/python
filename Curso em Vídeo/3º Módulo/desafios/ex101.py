
def voto(ano):
    from datetime import datetime
    anoAtual = datetime.now().year
    """
    -> Verifica se a pessoa pode votar ou não
    :param ano: Anos de nascimento da pessoa
    :return: Se a pessoa é obrigada a votar, opcional ou negada.
    """
    idade = anoAtual - ano
    if idade < 16:
        return f'   .Com {idade} anos: NEGADO'
    elif (18 > idade >= 16) or ( idade > 65):
        return f'   .Com {idade} anos: OPCIONAL'
    else:
        return f'   .Com {idade} anos: OBRIGATÓRIO'

print()
anoNasc = int(input('   .Informe seu ano de nascimento: '))
print(voto(anoNasc))
print()