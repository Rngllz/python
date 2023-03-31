pt = int(input("Primeiro termo: "))
rz = int(input("Razão: "))
decimo = pt + (10 - 1) * rz
for c in range(pt,decimo + rz,rz):
    print(c,end=' . ')
print("FIM")