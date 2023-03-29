from datetime import date
data = date.today().year

g = 0
p = 0

for c in range(1,8,1):
    ano = int(input("Ano de nascimento da {}ª pessoa: ".format(c)))
    if data - ano >= 21:
        g += 1
    else:
        p += 1

print('''\nMaiores de idade: {}
Menores de idade: {}
'''.format(g,p))