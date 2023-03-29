
maior = 0
menor = 0

for c in range(1,6,1):
    peso = float(input("Peso da {}ª pessoa: ".format(c)))
    if c == 1:
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso


print("\n\033[31mO maior peso lido é de {}.kg\n\033[32mO menor peso lido é de {}kg.\033[m".format(maior,menor))