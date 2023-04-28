jogador = dict()
gol = list()
time = list()
partidas = maior_partidas = num = opc = 0
cont = -1
r = ''

while r != 'N':
    gol.clear()
    print("_"*52)
    print()
    jogador['nome'] = str(input('   .Nome do Jogador: '))
    partidas = int(input(f'   .Quantas partidas {jogador["nome"]} jogou? '))

    print()
    for c in range(0,partidas):
        gol.append(int(input(f'     -| Quantos gols foram marcados na {c+1}ª partida? ')))
    print()

    jogador['gols'] = gol[:]
    
    if partidas > maior_partidas:
        maior_partidas = partidas
        num = len(str(jogador['gols']))

    jogador['total'] = sum(gol)
    time.append(jogador.copy())

    r = str(input('   .Continuar [S/N]: ')).strip().upper()[0]
    print()

print("_"*52)
print()
print()
print("    "+"_"*(30+num))
print(f'   |{"TABELA DE INFORMAÇÕES":^{30+num}}|')
print("    "+"‾"*(30+num))
for j in time:
    cont += 1
    print(f'    {cont:<10}{j["nome"]:<10}{str(j["gols"]):<{num+5}}{j["total"]}')
print("    "+"_"*(30+num))
print(f'   |{"cod":<10}{"nome":<10}{"gols":<10}{"total":>{num}}|')
print("    "+"‾"*(30+num))

while True:
    print()
    print()
    opc = int(input('    Mostrar dados do jogador: /cod='))

    print()
    if opc == 999:
        break

    if opc <= (len(time) -1):
        print(f'     .Levantamento do jogador {time[opc]["nome"].upper()}')
        for n,c in enumerate(time[opc]["gols"]):
            print(f'     .Na {n+1}ª partida foram feitos: {c} gols')
    else:
        print('     .Código errado!!! Tente novamente.')

print('    !------ PROGRAMA FINALIZADO ------!')
