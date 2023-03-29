n = int(input("Número: "))
print(("\033[33m{:=^20}").format(" TABUADA "))
for c in range(1,11,1):
    print("\033[32m{:>6} x {} = {}\033[m".format(n,c,n*c))
