
def notas(*lst,sit=False):
    """
    -> Função para analisar notas e situações de vários alunos
    Args:
        sit (bool, optional): Define se será mostrado ou não a situação do aluno. Defaults to False.
        lst (int): Recebe todas as notas dos alunos, em formatdo de tupla
    Returns:
        [dict]: Retorna um dicionário com o total de alunos, a maior e menor nota, a média da turma.
    """
    turma = dict()
    turma['total'] = len(lst)
    turma['maior'] = max(lst)
    turma['menor'] = min(lst)
    turma['média'] = sum(lst) / len(lst)

    if sit:
        if turma['média'] < 6:
            turma['situação'] = 'RUIM'
        elif turma['média'] == 6:
            turma['situação'] = 'RAZOÁVEL'
        else:
            turma['situação'] = 'BOM'

    return turma


resp = notas(5.5,2.5,8.5,sit=True)
print(resp)