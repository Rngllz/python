
# Meu código

num = int(input("Digite um número: "))
fat = num

print("{}! = {}".format(num,num),end='')
while num != 0:
    num -= 1
    if num != 0:
        fat = fat * (num)  
        print(" x {}".format(num),end='')
print(" = {}".format(fat))


num = int(input("\n\nDigite um número: "))
fat = num
for c in range(num-1,0,-1):
    fat = fat * c
print("O fatorial é: {}".format(fat))


# Código do professor


n = int(input("Digite um número: "))
c = n
f = 1

print('Calculando {}! = '.format(n),end='')
while c > 0:
    print('{}'.format(c),end='')
    print(' x ' if c > 1 else ' = ',end='')
    f *= c
    c -= 1
print(f)