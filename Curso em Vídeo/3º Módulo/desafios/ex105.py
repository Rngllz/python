
def notas(*lst,sit=False):
    turma = dict()
    maior = lst[0]
    menor = lst[0]
    for c in lst:
        if c > maior:
            maior = c
        if c < menor:
            menor = c
    turma['total'] = len(lst)
    turma['maior'] = maior
    turma['menor'] = menor
    turma['média'] = sum(lst) / len(lst)

    if sit == True:
        if turma['média'] < 6:
            turma['situação'] = 'RUIM'
        elif turma['média'] == 6:
            turma['situação'] = 'RAZOÁVEL'
        else:
            turma['situação'] = 'BOM'

    return turma


resp = notas(6,6,6,sit=True)
print(resp)