pessoa = dict()
grupo = list()
r = ''
acumulo = 0

while r != 'N':
    print()
    pessoa['nome'] = str(input('    Seu nome: '))
    pessoa['sexo'] = str(input('    Sexo [M/F]: ')).upper()
    pessoa['idade'] = int(input('    Sua idade: '))
    acumulo += pessoa['idade']
    grupo.append(pessoa.copy())
    r = str(input('    - Continuar [S/N]: ')).strip().upper()[0]

print()
print()
print(f'        .Foram cadastradas {len(grupo)} pessoas.')
print(f'        .A média de idade do grupo é de {acumulo/len(grupo):5.2f} anos.')

print()
print(f'        {" Lista de Mulheres ":=^40}')
for c in grupo:
    if c['sexo'] == 'F':
        print(f'            - {c["nome"]}, {c["idade"]} anos.')

print()
print(f'        {" Lista de Maioridade ":=^40}')
for c in grupo:
    if c['idade'] >= 18:
        print(f'            - {c["nome"]} - {c["sexo"]}, {c["idade"]} anos.')