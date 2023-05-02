

def ficha(nome, gols):
    """
    -> formata o texto de quantos gols x jogador fez
    Args:
        nome (str): nome do jogador
        gols (str): quantidade de gols que o jogador fez
    """
    if nome == '':
        nome='<desconhecido>'
    if gols == '':
        gols = '0'
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


nome = str(input('Nome do Jogador: '))
gols = str(input('Número de Gols: '))

ficha(nome,gols)