alunos = dict()
media = 0

for i in range(1,4):
    nome = str(input('Digite seu nome: '))
    nota = float(input('Digite sua nota: '))
    alunos[nome] = nota


for n in alunos.values():
    media += n

print(f'A média geral é: {media/3}')