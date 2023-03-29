pt = float(input("Primeiro termo: "))
rz = float(input("Razão: "))

print(pt,". ",end='')
for c in range(1,11,1):
    pt += rz
    print(pt,". ",end='')