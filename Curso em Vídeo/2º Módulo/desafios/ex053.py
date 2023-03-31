frase = str(input("Sua frase: ")).replace(' ','').upper()
tf = False

inverso = ''

#Meu código
for c in range(0,len(frase),1):
    if frase[0+c] == frase[len(frase)-1-c]:
        tf = True
print("É um palíndromo." if tf else "Não é um palíndromo,")

#Código do Professor
for letra in range(len(frase) -1 , -1 , -1):
    inverso += frase[letra].upper()
    if inverso == frase:
        tf = True
print("É um palíndromo." if tf else "Não é um palíndromo,")

# Macete para fazer sem o for
# inverso = frase[::-1]
# TRANSFORMA A PALAVRA NO REVERSO