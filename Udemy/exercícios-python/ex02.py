tempo = float(input('Tempo da viagem: h'))
velocidade = float(input('Velocidade média: kmh'))

distancia = velocidade * tempo
litro = distancia / 12

print(f'Em uma viagem de {tempo} horas, a uma velocidade de {velocidade}kmh')
print(f'Foram percorridos {distancia}km, e gastos {round(litro,2)}L de gasolina')