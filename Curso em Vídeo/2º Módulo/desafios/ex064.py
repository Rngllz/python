# Meu código:

num = cont = acúmulo = 0

while num != 999:
    num = int(input("Digite um número: "))
    if num != 999:
        cont += 1
        acúmulo += num

print("\nForam lidos {} números\nA soma de todos os números é igual a: {}".format(cont,acúmulo))


# Código do professor:

num = cont = acúmulo = 0
num = int(input("Digite um número: "))
while num != 999:
    cont += 1
    acúmulo += num
    num = int(input("Digite um número: "))
print("\nForam lidos {} números\nA soma de todos os números é igual a: {}".format(cont,acúmulo))