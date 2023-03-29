n = int(input("Número: "))

tf = True

for c in range(2,n,1):
    if n%c == 0:
        tf = False

print("É um Número primo" if tf else "Não é um Número primo")