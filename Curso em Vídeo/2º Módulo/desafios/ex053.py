frase = str(input("Sua frase: ")).replace(' ','')
tf = True

for c in range(0,len(frase),1):
    if frase[0+c] != frase[len(frase)-1-c]:
        tf = False

print("É um palíndromo." if tf else "Não é um palíndromo,")