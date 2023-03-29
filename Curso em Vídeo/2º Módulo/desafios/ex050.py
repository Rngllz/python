s = 0

for c in range(1,7,1):
    n = int(input("{}º Número: ".format(c)))
    if n%2 == 0:
        s += n
print("\033[33mO resultado é: \033[32m{}\033[m".format(s))