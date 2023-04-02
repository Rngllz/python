'''pt = int(input("Primeiro termo: ")) # onde começa
rz = int(input("Razão: ")) # de quanto em quanto
num = 0
r = -1

while r != 0:

    num = 0
    if r == -1:
        decimo = pt + (10 -1) * rz # onde termina
    else:
        decimo = pt + (10 + r -1) * rz # onde termina 
    while num != decimo:
        num = num + rz
        print(num,end='. ') 

    print("FIM")
    r = int(input("Deseja mostrar mais quantos termos: "))
'''


num = 0
termo = 10
quant_termo = termo
cont = 1

pt = int(input("Primeiro termo: ")) # onde começa
rz = int(input("Razão: ")) # de quanto em quanto

while termo > 0:
    cont = 1
    while cont <= termo:
        num += rz
        print(num,end='. ') 
        cont += 1

    print('')
    termo = int(input("Mais quantos termos: "))
    quant_termo += termo

print("Foram feitos {} termos.".format(quant_termo))
print('FIM')