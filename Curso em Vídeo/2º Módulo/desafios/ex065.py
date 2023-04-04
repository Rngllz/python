r = 'S'
cont = acúmulo = maior = menor = 0

while r == 'S':
    num = int(input("Digite um número: "))
    cont += 1
    acúmulo += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    r = str(input("Deseja continuar [S|N]: ")).upper().strip()[0]

print("A média de {} números resulta em: {}".format(cont,acúmulo / cont))
print("O maior número lido é: {}\nO menor número lido é: {}".format(maior,menor))