'''pessoas = {'nome':'Gustavo', 'sexo':'M', 'idade': 22}
del pessoas['sexo']
pessoas['nome'] = 'Leandro'
print(pessoas)
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos de vida.')

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k, v in pessoas.items():
    print(f'{k} = {v}') '''

'''
brasil = []
estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf':'São Paulo', 'sigla':'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[0]['uf'])'''

estado = dict()
brasil = list()

for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k,v in e.items():
        print(f' {k} = {v}')


print(brasil)
print(brasil[1]['sigla'])