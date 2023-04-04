'''num = int(input("Número inteiro: "))
quantidade = int(input("Qual o tamanho da sequéncia: "))
c =0
ant_num = 0

print("\n")

while c != quantidade:
    c +=1
    num = num + ant_num
    ant_num = ant_num + num
    print("{} -> {} -> ".format(num, ant_num),end='')

print("FIM")'''


# Meu código

c = 0
num = 0
ant_num = 1
sequencia = int(input("\nQuntos termos você quer mostrar: \033[32m"))
print("\033[m")
print('\033[33m~'*sequencia*5)  

print('{} -> '.format(0),end='') 

while c <= (sequencia -1):      
    c += 1
    if c < (sequencia -1):
        ant_num = num + ant_num
        print('{} -> '.format(ant_num),end='')
    if c <= (sequencia -1):
        num = num + ant_num
        print('{} -> '.format(num),end='')
    c += 1
print('\033[mFIM')
print('\033[33m~'*sequencia*5)
print('\033[m')



# Código do professor

n = int(input('Quantos termos você quer mostrar: '))
t1 = 0
t2 = 1
cont = 3
print('~'*30)
print('{} - {}'.format(t1,t2), end='')
while cont <= n:
    t3 = t1 + t2
    print(' - {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' - FIM')

# 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
#                t1   t2   t3