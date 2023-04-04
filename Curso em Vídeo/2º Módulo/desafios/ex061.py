pt = int(input("Primeiro termo: ")) # onde começa
rz = int(input("Razão: ")) # de quanto em quanto
num = 0
cont = 1

while cont <= 10:
    num += rz
    print(num,end='. ') 
    cont += 1

print('FIM')