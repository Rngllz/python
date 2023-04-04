acumulo = 0
media = 0
idade_maior = 0
homem_mais_velho = ''
cont_mulher = 0

for c in range(1,5,1):
    print("\n\033[35mINFORMAÇÕES. {}ª .PESSOA\033[m".format(c))
    nome = str(input("Seu nome: "))
    idade = int(input("Sua idade: "))
    sexo = int(input("Sexo (1-masc 0-fem): "))

    acumulo += idade

    if sexo == 1:
        if idade > idade_maior:
            idade_maior = idade
            homem_mais_velho = nome
    else:
        if idade < 20:
            cont_mulher += 1

print("\n\033[36m{:=^51}".format("* INFORMAÇÕES *"))
print("\033[m A média de todas as idade é: {}.".format(acumulo/4))
print(" O nome do homem mais velho ({} anos de idade) é: {}".format(idade_maior,homem_mais_velho))
print(" Quantidade de mulheres com menos de 20 anos: {}".format(cont_mulher))
print("\033[36m{:=^51}\033[m\n".format(""))