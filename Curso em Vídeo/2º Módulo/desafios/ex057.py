
# Meu código

sexo = ''

while sexo != 'M' and sexo != 'F':

    sexo = str(input("Digite o seu sexo [M / F]: ")).upper()
    
    if sexo != 'M' and sexo != 'F':
        print("\033[31mPerdão. Dado inválido, repita novamente...\033[m")

print("Você é homem." if sexo == 'M' else "Você é mulher.")


# Código do professor

sexo = str(input('Informe seu sexo: [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input("Dados inválidos. Por favor, informe seu sexo: ")).strip().upper()[0]
print("Sexo {} registado com sucesso".format(sexo))