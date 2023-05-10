media = 0
for c in range(1,6):
    nota = float(input(f'Digite a {c}ª nota: '))
    media += nota
print(f'A média entre as {c} notas é: {media/c}')


print()

n = 0
media2 = 0
while n < 5:
    n += 1
    nota2 = float(input(f'Sua {n}ª nota: '))
    media2 += nota2
    
print(f'A sua média é: {media2 / n}')