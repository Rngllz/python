
def ler():
    tempo = float(input('Tempo gasto na viagem: '))
    velocidade = float(input('Velocidade média durante ela: '))
    print(f'Tempo: {tempo}\nVelocidade: {velocidade}')
    return tempo,velocidade


def c_distancia(tv):
    print(f'Distância: {tv[0] * tv[1]}')
    return tv[0] * tv[1]


def c_litros(d):
    print(f'Litros: {round(d / 12,2)}')
    return d / 12




c_litros(c_distancia(ler()))