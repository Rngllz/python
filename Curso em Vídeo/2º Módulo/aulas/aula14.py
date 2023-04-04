'''for c in range(1,11):
    print(c)'''

c = 1

while c <= 10:
    print(c)
    c += 1


par = 0
impar = 0
n = 1
while n != 0:
    n = int(input("Digite um número: "))
    if n != 0:
        if n%2 == 0:
            par += 1
        else:
            impar += 1
print("Foram {} números pares e {} ímpares".format(par,impar))

r = 'S'
while r == "S":
    r = str(input("Quer continuar [S|N]: ")).upper()
